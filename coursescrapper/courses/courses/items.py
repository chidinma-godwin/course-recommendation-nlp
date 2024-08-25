# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CoursesItem(scrapy.Item):
    course_name = scrapy.Field()
    course_type = scrapy.Field()
    level = scrapy.Field()
    has_certificate = scrapy.Field()
    provider = scrapy.Field()
    subject = scrapy.Field()
    num_rating = scrapy.Field()
    avg_rating = scrapy.Field()
    is_university = scrapy.Field()
    institution = scrapy.Field()
    description = scrapy.Field()
    duration = scrapy.Field()
    start_date = scrapy.Field()
    pricing = scrapy.Field()
    link = scrapy.Field()
    additional_course_detail = scrapy.Field()
