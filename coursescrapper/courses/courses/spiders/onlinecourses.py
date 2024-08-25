import scrapy
import json
from courses.items import CoursesItem  


class OnlinecoursesSpider(scrapy.Spider):
    name = "onlinecourses"
    allowed_domains = ["classcentral.com"]
    start_urls = ["https://www.classcentral.com/subject/programming-and-software-development?lang=english",
                  "https://www.classcentral.com/subject/cs?lang=english",
                  "https://www.classcentral.com/subject/data-science?lang=english",
                  "https://www.classcentral.com/subject/certifications?lang=english"]

    def parse(self, response):
        courses = response.xpath('//li[@itemprop="itemListElement"]')
        
        for course in courses:
            course_item = CoursesItem()
                
            details = json.loads(course.css("a.course-name::attr(data-track-props)").get())
            best_of_all_time_text = course.xpath('//a[href="/collection/top-free-online-courses"]/text()').get()
            course_url = f"https://www.classcentral.com{course.css('a.course-name::attr(href)').get()}"
            
            course_item['course_name'] = details['course_name']
            course_item['course_type'] = details['course_type']
            course_item['level'] = details['course_level']
            course_item['has_certificate'] = details['course_certificate']
            course_item['provider'] = details['course_provider']
            course_item['subject'] = details['course_subject']
            course_item['num_rating'] = details['course_num_rating']
            course_item['avg_rating'] = details['course_avg_rating']
            course_item['is_university'] = details['course_is_university']
            course_item['institution'] = details['course_institution']
            course_item['course_is_classroom'] = details['course_is_classroom']
            course_item['description'] = course.xpath("//p/a[@data-track-click='course_click']/text()").get()
            course_item['duration'] = course.xpath("//span[@aria-label='Workload and duration']/text()").get()
            course_item['start_date'] = course.xpath("//span[@aria-label='Start date']/text()").get()
            course_item['pricing'] = course.xpath("//span[@aria-label='Pricing']/text()").get()
            course_item['link'] = course_url if course_item['course_is_classroom'] else f"{course_url}/visit"
            
            yield response.follow(course_url, callback=self.parse_course_page, cb_kwargs=dict(course_item=course_item))
            
        next_page_details = response.xpath("//button[@data-name='LOAD_MORE']/@data-detail").get()
        if next_page_details is not None:
            next_details = json.loads(next_page_details)
            next_page = next_details['page']
            next_page_url = f"https://www.classcentral.com/subject/{details['cc_source_slug']}?lang=english&page={next_page}"
            yield response.follow(next_page_url, callback=self.parse)
        

    def parse_course_page(self, response, course_item):
        if course_item['course_is_classroom']:
            course_item['additional_course_detail'] = response.css("li.classroom-item span.text-3::text").getall()
        else:
            course_item['additional_course_detail'] = response.xpath('//div[contains(@class, "wysiwyg")]/text() |       //div[contains(@class, "wysiwyg")]/p/text() | //div[contains(@class, "wysiwyg")]/strong/text()').getall()
        
        yield course_item