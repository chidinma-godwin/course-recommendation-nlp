# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CoursesItem(scrapy.Item):
    course_name = scrapy.Field()
    course_type = scrapy.Field()
    course_level = scrapy.Field()
    course_certificate = scrapy.Field()
    course_provider = scrapy.Field()
    course_subject = scrapy.Field()
    course_num_rating = scrapy.Field()
    course_avg_rating = scrapy.Field()
    course_is_university = scrapy.Field()
    course_institution = scrapy.Field()
    course_is_classroom = scrapy.Field()
    description = scrapy.Field()
    duration = scrapy.Field()
    start_date = scrapy.Field()
    pricing = scrapy.Field()
    is_all_time_best = scrapy.Field()
    course_link = scrapy.Field()
    additional_course_detail = scrapy.Field()
    teacher = scrapy.Field()
