from maker.models import HomePage, About, Join, Contact
from mezzanine.core.admin import DisplayableAdmin
from mezzanine.pages.admin import PageAdmin
from copy import deepcopy
from django.contrib import admin

class HomePageAdmin(DisplayableAdmin):
    fieldsets = [
        ("Title",               {'fields': ['title']}),
        ("Published Date",               {'fields': ['publish_date']}),
        ("Published Status",               {'fields': ['status', 'is_homepage']}),
        ("Home",               {'fields': ['welcome_message','videoid_youtube','image_join_cta', 'image_stats']}),
    ]

    list_display = ('title', 'status', 'publish_date','videoid_youtube')
#    list_editable = ('videoid_youtube',)

about_extra_fieldsets = (
    ('Header', {"fields": ("headerimg",)}),
    ('AboutText', {"fields": ("abouttext",)}),
)
class AboutAdmin(PageAdmin):
    fieldsets = deepcopy(PageAdmin.fieldsets) + about_extra_fieldsets


join_extra_fieldsets = (
    ('Header', {"fields": ("headerimg",)}),
    ('Marketing Message', {"fields": ("marketing_message",)}),
    ('Thank You Message', {"fields": ("thankyou_message",)}),
)
class JoinAdmin(PageAdmin):
    fieldsets = deepcopy(PageAdmin.fieldsets) + join_extra_fieldsets

    
contact_extra_fieldsets = (
    ('Header', {"fields": ("headerimg",)}),
    ('Contact Page Message', {"fields": ("contact_page_message",)}),
    ('Thank You Message', {"fields": ("thankyou_message",)}),
)
class ContactAdmin(PageAdmin):
    fieldsets = deepcopy(PageAdmin.fieldsets) + contact_extra_fieldsets


#Job_extra_fieldsets = (
#    ('Job Opportunity', {"fields": ("job_post",)}),
#)
#class JobAdmin(PageAdmin):
#    fieldsets = deepcopy(PageAdmin.fieldsets) + Job_extra_fieldsets
#
#
#news_extra_fieldsets = (
#    ('News Image', {"fields": ("headerimg",)}),
#    ('News URL', {"fields": ("news_url","news_url_target")}),
#    ('Author', {"fields": ("author",)}),
#    ('News Copy', {"fields": ("news_text",)}),
#)
#class NewsItemAdmin(PageAdmin):
#    fieldsets = deepcopy(PageAdmin.fieldsets) + news_extra_fieldsets
#
#experts_blog_extra_fieldsets = (
#    ('Post Image', {"fields": ("headerimg",)}),
#    ('Featured Post?', {"fields": ("is_featured",)}),
#    ('Author', {"fields": ("author",)}),
#    ('Blog Copy', {"fields": ("blog_text",)}),
#)
#class ExpertsBlogItemAdmin(PageAdmin):
#    fieldsets = deepcopy(PageAdmin.fieldsets) + experts_blog_extra_fieldsets


#admin.site.register(ExpertsBlogItem, ExpertsBlogItemAdmin)
#admin.site.register(NewsItem, NewsItemAdmin)
#admin.site.register(Job, JobAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Join, JoinAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(HomePage, HomePageAdmin)