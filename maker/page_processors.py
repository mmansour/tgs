from django import forms
from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect
from mezzanine.pages.page_processors import processor_for
from maker.models import Join, Contact
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from mezzanine.utils.views import paginate

COUNTRIES = (
    ('COUNTRY', _(u'Country')),
    ('AF', _(u'Afghanistan')),
    ('AX', _(u'\xc5land Islands')),
    ('AL', _(u'Albania')),
    ('DZ', _(u'Algeria')),
    ('AS', _(u'American Samoa')),
    ('AD', _(u'Andorra')),
    ('AO', _(u'Angola')),
    ('AI', _(u'Anguilla')),
    ('AQ', _(u'Antarctica')),
    ('AG', _(u'Antigua and Barbuda')),
    ('AR', _(u'Argentina')),
    ('AM', _(u'Armenia')),
    ('AW', _(u'Aruba')),
    ('AU', _(u'Australia')),
    ('AT', _(u'Austria')),
    ('AZ', _(u'Azerbaijan')),
    ('BS', _(u'Bahamas')),
    ('BH', _(u'Bahrain')),
    ('BD', _(u'Bangladesh')),
    ('BB', _(u'Barbados')),
    ('BY', _(u'Belarus')),
    ('BE', _(u'Belgium')),
    ('BZ', _(u'Belize')),
    ('BJ', _(u'Benin')),
    ('BM', _(u'Bermuda')),
    ('BT', _(u'Bhutan')),
    ('BO', _(u'Bolivia, Plurinational State of')),
    ('BQ', _(u'Bonaire, Sint Eustatius and Saba')),
    ('BA', _(u'Bosnia and Herzegovina')),
    ('BW', _(u'Botswana')),
    ('BV', _(u'Bouvet Island')),
    ('BR', _(u'Brazil')),
    ('IO', _(u'British Indian Ocean Territory')),
    ('BN', _(u'Brunei Darussalam')),
    ('BG', _(u'Bulgaria')),
    ('BF', _(u'Burkina Faso')),
    ('BI', _(u'Burundi')),
    ('KH', _(u'Cambodia')),
    ('CM', _(u'Cameroon')),
    ('CA', _(u'Canada')),
    ('CV', _(u'Cape Verde')),
    ('KY', _(u'Cayman Islands')),
    ('CF', _(u'Central African Republic')),
    ('TD', _(u'Chad')),
    ('CL', _(u'Chile')),
    ('CN', _(u'China')),
    ('CX', _(u'Christmas Island')),
    ('CC', _(u'Cocos (Keeling) Islands')),
    ('CO', _(u'Colombia')),
    ('KM', _(u'Comoros')),
    ('CG', _(u'Congo')),
    ('CD', _(u'Congo, The Democratic Republic of the')),
    ('CK', _(u'Cook Islands')),
    ('CR', _(u'Costa Rica')),
    ('CI', _(u"C\xf4te D'ivoire")),
    ('HR', _(u'Croatia')),
    ('CU', _(u'Cuba')),
    ('CW', _(u'Cura\xe7ao')),
    ('CY', _(u'Cyprus')),
    ('CZ', _(u'Czech Republic')),
    ('DK', _(u'Denmark')),
    ('DJ', _(u'Djibouti')),
    ('DM', _(u'Dominica')),
    ('DO', _(u'Dominican Republic')),
    ('EC', _(u'Ecuador')),
    ('EG', _(u'Egypt')),
    ('SV', _(u'El Salvador')),
    ('GQ', _(u'Equatorial Guinea')),
    ('ER', _(u'Eritrea')),
    ('EE', _(u'Estonia')),
    ('ET', _(u'Ethiopia')),
    ('FK', _(u'Falkland Islands (Malvinas)')),
    ('FO', _(u'Faroe Islands')),
    ('FJ', _(u'Fiji')),
    ('FI', _(u'Finland')),
    ('FR', _(u'France')),
    ('GF', _(u'French Guiana')),
    ('PF', _(u'French Polynesia')),
    ('TF', _(u'French Southern Territories')),
    ('GA', _(u'Gabon')),
    ('GM', _(u'Gambia')),
    ('GE', _(u'Georgia')),
    ('DE', _(u'Germany')),
    ('GH', _(u'Ghana')),
    ('GI', _(u'Gibraltar')),
    ('GR', _(u'Greece')),
    ('GL', _(u'Greenland')),
    ('GD', _(u'Grenada')),
    ('GP', _(u'Guadeloupe')),
    ('GU', _(u'Guam')),
    ('GT', _(u'Guatemala')),
    ('GG', _(u'Guernsey')),
    ('GN', _(u'Guinea')),
    ('GW', _(u'Guinea-bissau')),
    ('GY', _(u'Guyana')),
    ('HT', _(u'Haiti')),
    ('HM', _(u'Heard Island and McDonald Islands')),
    ('VA', _(u'Holy See (Vatican City State)')),
    ('HN', _(u'Honduras')),
    ('HK', _(u'Hong Kong')),
    ('HU', _(u'Hungary')),
    ('IS', _(u'Iceland')),
    ('IN', _(u'India')),
    ('ID', _(u'Indonesia')),
    ('IR', _(u'Iran, Islamic Republic of')),
    ('IQ', _(u'Iraq')),
    ('IE', _(u'Ireland')),
    ('IM', _(u'Isle of Man')),
    ('IL', _(u'Israel')),
    ('IT', _(u'Italy')),
    ('JM', _(u'Jamaica')),
    ('JP', _(u'Japan')),
    ('JE', _(u'Jersey')),
    ('JO', _(u'Jordan')),
    ('KZ', _(u'Kazakhstan')),
    ('KE', _(u'Kenya')),
    ('KI', _(u'Kiribati')),
    ('KP', _(u"Korea, Democratic People's Republic of")),
    ('KR', _(u'Korea, Republic of')),
    ('KW', _(u'Kuwait')),
    ('KG', _(u'Kyrgyzstan')),
    ('LA', _(u"Lao People's Democratic Republic")),
    ('LV', _(u'Latvia')),
    ('LB', _(u'Lebanon')),
    ('LS', _(u'Lesotho')),
    ('LR', _(u'Liberia')),
    ('LY', _(u'Libyan Arab Jamahiriya')),
    ('LI', _(u'Liechtenstein')),
    ('LT', _(u'Lithuania')),
    ('LU', _(u'Luxembourg')),
    ('MO', _(u'Macao')),
    ('MK', _(u'Macedonia, The Former Yugoslav Republic of')),
    ('MG', _(u'Madagascar')),
    ('MW', _(u'Malawi')),
    ('MY', _(u'Malaysia')),
    ('MV', _(u'Maldives')),
    ('ML', _(u'Mali')),
    ('MT', _(u'Malta')),
    ('MH', _(u'Marshall Islands')),
    ('MQ', _(u'Martinique')),
    ('MR', _(u'Mauritania')),
    ('MU', _(u'Mauritius')),
    ('YT', _(u'Mayotte')),
    ('MX', _(u'Mexico')),
    ('FM', _(u'Micronesia, Federated States of')),
    ('MD', _(u'Moldova, Republic of')),
    ('MC', _(u'Monaco')),
    ('MN', _(u'Mongolia')),
    ('ME', _(u'Montenegro')),
    ('MS', _(u'Montserrat')),
    ('MA', _(u'Morocco')),
    ('MZ', _(u'Mozambique')),
    ('MM', _(u'Myanmar')),
    ('NA', _(u'Namibia')),
    ('NR', _(u'Nauru')),
    ('NP', _(u'Nepal')),
    ('NL', _(u'Netherlands')),
    ('NC', _(u'New Caledonia')),
    ('NZ', _(u'New Zealand')),
    ('NI', _(u'Nicaragua')),
    ('NE', _(u'Niger')),
    ('NG', _(u'Nigeria')),
    ('NU', _(u'Niue')),
    ('NF', _(u'Norfolk Island')),
    ('MP', _(u'Northern Mariana Islands')),
    ('NO', _(u'Norway')),
    ('OM', _(u'Oman')),
    ('PK', _(u'Pakistan')),
    ('PW', _(u'Palau')),
    ('PS', _(u'Palestinian Territory, Occupied')),
    ('PA', _(u'Panama')),
    ('PG', _(u'Papua New Guinea')),
    ('PY', _(u'Paraguay')),
    ('PE', _(u'Peru')),
    ('PH', _(u'Philippines')),
    ('PN', _(u'Pitcairn')),
    ('PL', _(u'Poland')),
    ('PT', _(u'Portugal')),
    ('PR', _(u'Puerto Rico')),
    ('QA', _(u'Qatar')),
    ('RE', _(u'R\xe9union')),
    ('RO', _(u'Romania')),
    ('RU', _(u'Russian Federation')),
    ('RW', _(u'Rwanda')),
    ('BL', _(u'Saint Barth\xe9lemy')),
    ('SH', _(u'Saint Helena, Ascension and Tristan Da Cunha')),
    ('KN', _(u'Saint Kitts and Nevis')),
    ('LC', _(u'Saint Lucia')),
    ('MF', _(u'Saint Martin (French Part)')),
    ('PM', _(u'Saint Pierre and Miquelon')),
    ('VC', _(u'Saint Vincent and the Grenadines')),
    ('WS', _(u'Samoa')),
    ('SM', _(u'San Marino')),
    ('ST', _(u'Sao Tome and Principe')),
    ('SA', _(u'Saudi Arabia')),
    ('SN', _(u'Senegal')),
    ('RS', _(u'Serbia')),
    ('SC', _(u'Seychelles')),
    ('SL', _(u'Sierra Leone')),
    ('SG', _(u'Singapore')),
    ('SX', _(u'Sint Maarten (Dutch Part)')),
    ('SK', _(u'Slovakia')),
    ('SI', _(u'Slovenia')),
    ('SB', _(u'Solomon Islands')),
    ('SO', _(u'Somalia')),
    ('ZA', _(u'South Africa')),
    ('GS', _(u'South Georgia and the South Sandwich Islands')),
    ('SS', _(u'South Sudan')),
    ('ES', _(u'Spain')),
    ('LK', _(u'Sri Lanka')),
    ('SD', _(u'Sudan')),
    ('SR', _(u'Suriname')),
    ('SJ', _(u'Svalbard and Jan Mayen')),
    ('SZ', _(u'Swaziland')),
    ('SE', _(u'Sweden')),
    ('CH', _(u'Switzerland')),
    ('SY', _(u'Syrian Arab Republic')),
    ('TW', _(u'Taiwan, Province of China')),
    ('TJ', _(u'Tajikistan')),
    ('TZ', _(u'Tanzania, United Republic of')),
    ('TH', _(u'Thailand')),
    ('TL', _(u'Timor-leste')),
    ('TG', _(u'Togo')),
    ('TK', _(u'Tokelau')),
    ('TO', _(u'Tonga')),
    ('TT', _(u'Trinidad and Tobago')),
    ('TN', _(u'Tunisia')),
    ('TR', _(u'Turkey')),
    ('TM', _(u'Turkmenistan')),
    ('TC', _(u'Turks and Caicos Islands')),
    ('TV', _(u'Tuvalu')),
    ('UG', _(u'Uganda')),
    ('UA', _(u'Ukraine')),
    ('AE', _(u'United Arab Emirates')),
    ('GB', _(u'United Kingdom')),
    ('US', _(u'United States')),
    ('UM', _(u'United States Minor Outlying Islands')),
    ('UY', _(u'Uruguay')),
    ('UZ', _(u'Uzbekistan')),
    ('VU', _(u'Vanuatu')),
    ('VE', _(u'Venezuela, Bolivarian Republic of')),
    ('VN', _(u'Viet Nam')),
    ('VG', _(u'Virgin Islands, British')),
    ('VI', _(u'Virgin Islands, U.S.')),
    ('WF', _(u'Wallis and Futuna')),
    ('EH', _(u'Western Sahara')),
    ('YE', _(u'Yemen')),
    ('ZM', _(u'Zambia')),
    ('ZW', _(u'Zimbabwe')),
)


VIEWS_PER_MONTH = (
    ('Views_Per_Month', _(u'Views Per Month')),
    ('0-100K', _(u'0-100K')),
    ('100K-500K', _(u'100K-500K')),
    ('500K-3M', _(u'500K-3M')),
    ('3M+', _(u'3M+')),
)

VIEWS_PER_VIDEO = (
    ('Views_Per_Video', _(u'Views Per Video')),
    ('10K-50K', _(u'10K-50K')),
    ('50K-300K', _(u'50K-300K')),
    ('300K+', _(u'300K+')),
)

YT_PARTNER = (
    ('Youtube_Partner?', _(u'Youtube Partner?')),
    ('No', _(u'No')),
    ('Yes', _(u'Yes')),
    ('Unsure', _(u'Unsure')),
)

GENRE = (
    ('Genre', _(u'Genre')),
    ('Comedy', _(u'Comedy')),
    ('Music', _(u'Music')),
)

class JoinForm(forms.Form):
    name = forms.CharField(initial='Name')
    email = forms.EmailField(initial='Email Address')
#    channel_names = forms.CharField(initial='Channel Names')
    channel_url = forms.CharField(initial='Channel URL', widget=forms.TextInput(attrs={'class' : 'longinput'}))
    youtube_partner = forms.ChoiceField(choices=YT_PARTNER, initial='Youtube_Partner?')
    number_of_subscribers = forms.CharField(initial='Number of Subscribers')
    average_views_month = forms.ChoiceField(choices=VIEWS_PER_MONTH, initial='Views_Per_Month')
    average_views_video = forms.ChoiceField(choices=VIEWS_PER_VIDEO, initial='Views_Per_Video')
    country = forms.ChoiceField(choices=COUNTRIES, initial='COUNTRY')
    city = forms.CharField(initial="City")
    language = forms.CharField(initial="Language")
    genre = forms.ChoiceField(choices=GENRE, initial='Genre')
#    message = forms.CharField(widget=forms.Textarea, initial="Tell us about yourself...", required=False)


@processor_for(Join)
def join_form(request, page):
    form = JoinForm(auto_id='%s')
    if request.method == "POST":
        form = JoinForm(request.POST, auto_id='%s')
        if form.is_valid():
            # Form processing goes here.
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            channel_url = form.cleaned_data['channel_url']
            youtube_partner = form.cleaned_data['youtube_partner']
            number_of_subscribers = form.cleaned_data['number_of_subscribers']
            average_views_month = form.cleaned_data['average_views_month']
            average_views_video = form.cleaned_data['average_views_video']
            country = form.cleaned_data['country']
            city = form.cleaned_data['city']
            language = form.cleaned_data['language']
            genre = form.cleaned_data['genre']

            message = 'Name={0}\n\
                email={1}\n\
                channel_url={2}\n\
                youtube_partner={3}\n\
                number_of_subscribers={4}\n\
                average_views_month={5}\n\
                average_views_video={6}\n\
                country={7}\n\
                city={8}\n\
                language={9}\n\
                genre={10}\n\
            '.format(name,
                     email,
                     channel_url,
                     youtube_partner,
                     number_of_subscribers,
                     average_views_month,
                     average_views_video,
                     country,
                     city,
                     language,genre)

            send_mail('Maker Channel Inquiry', message, 'info@makerstudios.com',
                    ['info@makerstudios.com'], fail_silently=False)
            redirect = request.path + "?submitted=true"
            return HttpResponseRedirect(redirect)
    return {"form": form}


SUBJECT = (
    ('Subject', _(u'Subject')),
    ('General-Inquiry', _(u'General Inquiry')),
    ('Press', _(u'Press')),
    ('Marketing', _(u'Marketing')),
    ('Sales', _(u'Sales')),
    ('Jobs', _(u'Jobs')),
)

class ContactForm(forms.Form):
    first_name = forms.CharField(initial='First Name')
    last_name = forms.CharField(initial='Last Name')
    email = forms.EmailField(initial='Email Address')
    subject = forms.ChoiceField(choices=SUBJECT, initial='Subject')
    message = forms.CharField(widget=forms.Textarea, initial="Message", required=False)

    
@processor_for(Contact)
def contact_form(request, page):
    form = ContactForm(auto_id='%s')
    if request.method == "POST":
        form = ContactForm(request.POST, auto_id='%s')
        if form.is_valid():
            # Form processing goes here.
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            message = 'First Name={0}\n\
                Last Name={1}\n\
                Email={2}\n\
                Subject={3}\n\
                Message={4}\n\
            '.format(first_name,
                     last_name,
                     email,
                     subject,
                     message)

            send_mail('TGS Contact Inquiry', message, 'info@makerstudios.com',
                    ['info@makerstudios.com'], fail_silently=False)
            redirect = request.path + "?submitted=true"
            return HttpResponseRedirect(redirect)
    return {"form": form}


#@processor_for("jobs")
#def get_jobs(request, page):
#    joblist = Job.objects.filter(status=2)
#    return {'joblist':joblist}

#@processor_for("news")
#def get_news(request, page):
#    newslist = NewsItem.objects.filter(status=2).order_by('-publish_date')
#    newslist = paginate(newslist,
#                        request.GET.get("page", 1),
#                        7, 7)
#    print request.GET.get("page")
#    if request.GET.get("page") == '1':
#        return HttpResponsePermanentRedirect('/news/')
#    else:
#        return {'newslist':newslist}

#@processor_for("experts-blog")
#def get_expert_blog_posts(request, page):
#    bloglist = ExpertsBlogItem.objects.filter(status=2).order_by('-publish_date')
#    bloglist = paginate(bloglist,
#                        request.GET.get("page", 1),
#                        7, 7)
#    featured_posts = ExpertsBlogItem.objects.filter(status=2)\
#        .filter(is_featured=True).order_by('-publish_date')
#
#    if request.GET.get("page") == '1':
#        return HttpResponsePermanentRedirect('/experts-blog/')
#    else:
#        return {'bloglist':bloglist, 'featured_posts':featured_posts}
#
#@processor_for(ExpertsBlogItem)
#def get_featured_posts(request, page):
#    featured_posts = ExpertsBlogItem.objects.filter(status=2)\
#        .filter(is_featured=True).order_by('-publish_date')
#    return {'featured_posts':featured_posts}