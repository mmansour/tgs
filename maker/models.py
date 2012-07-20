from django.db import models
from mezzanine.core.models import Displayable, RichTextField
from mezzanine.pages.models import Page
import logging

class HomePage(Displayable):
    welcome_message = RichTextField(blank=True, verbose_name="Welcome Message")
    videoid_youtube = models.CharField(max_length=20, verbose_name="Youtube Video ID", blank=True)
    image_join_cta = models.ImageField(upload_to='uploads', default='uploads/default-cta.jpg')
    image_stats = models.ImageField(upload_to='uploads', default='uploads/default-stats.jpg')
    is_homepage = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

class About(Page):
    headerimg = models.ImageField(upload_to='uploads', default='uploads/default-cta.jpg', null=True, blank=True)
    abouttext = RichTextField(blank=True, verbose_name="About Maker")

    def __unicode__(self):
        return self.title

class Join(Page):
    headerimg = models.ImageField(upload_to='uploads', default='uploads/default-cta.jpg', null=True, blank=True)
    marketing_message = RichTextField(blank=True, null=True, verbose_name="Marketing Message")
    thankyou_message = RichTextField(blank=True, null=True, verbose_name="Thank You for Joining Message")

    def __unicode__(self):
        return self.title

class Contact(Page):
    headerimg = models.ImageField(upload_to='uploads', default='uploads/default-cta.jpg', null=True, blank=True)
    contact_page_message = RichTextField(blank=True, null=True, verbose_name="Contact Page Message")
    thankyou_message = RichTextField(blank=True, null=True, verbose_name="Thank You for Contacting Message")

    def __unicode__(self):
        return self.title

#class Job(Page):
#    job_post = RichTextField(blank=True, null=True, verbose_name="Job Opportunity")
#
#    def __unicode__(self):
#        return self.title
#
#class NewsItem(Page):
#    headerimg = models.ImageField(upload_to='uploads', default='uploads/news-default_1.png', null=True, blank=True)
#    author = models.TextField(blank=True, null=True, verbose_name="Author")
#    news_text = RichTextField(blank=True, null=True, verbose_name="News Copy")
#    news_url = models.URLField(blank=True, null=True, verbose_name="News URL")
#    news_url_target = models.CharField(blank=True, null=True,
#                                       max_length=10,
#                                       verbose_name="To Open New Window use '_blank'. Same Window '_self'", default="_blank")
#
#    def __unicode__(self):
#        return self.title
#
#class ExpertsBlogItem(Page):
#    is_featured = models.BooleanField(default=False)
#    headerimg = models.ImageField(upload_to='uploads', default='uploads/blog-header.jpg', null=True, blank=True)
#    author = models.TextField(blank=True, null=True, verbose_name="Author")
#    blog_text = RichTextField(blank=True, null=True, verbose_name="Blog Copy")
#
#    def __unicode__(self):
#        return self.title
    


