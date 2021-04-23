from django.db.models import Manager
from django.shortcuts import render
from main.models import Categories, Advertise, Settings, ServicesHasAdvertise
from google_trans_new import google_translator
from django.db import connection


def custom_sql(q):
    with connection.cursor() as cursor:
        cursor.execute(q)
        row = cursor.fetchall()

    return row


def index(request, path):
    if request.GET:
        cid = request.GET['id']
        classy = Advertise.objects.get(id=cid)
        classy.views += 1
        classy.save()
    translator = google_translator()
    issue = int(Settings.objects.filter(id=1).values('svalue')[0]['svalue'])

    tClassies = Advertise.objects.filter(active=1, advertise_template_id__in=[1, 2, 7], end_issue__gte=issue,
                                         newspaper_content_en=None).order_by(
        '-id')
    for tClassy in tClassies:
        translate_text = translator.translate(tClassy.newspaper_content, lang_tgt='en')
        tClassy.newspaper_content_en = translate_text
        tClassy.save()
    categories = list(Categories.objects.all().values())
    if 'en' in path:
        lang = 'en'
    else:
        lang = 'ru'
    classys = custom_sql(f"""SELECT advertise.id, advertise.categories_id, advertise.newspaper_content, 
        advertise.newspaper_content_en, advertise.views, advertise.created, 
        GROUP_CONCAT('serv', services.id  SEPARATOR ' ') as services FROM advertise
        LEFT JOIN services_has_advertise sha ON sha.advertise_id = advertise.id
        LEFT JOIN services ON services.id = sha.services_id
        WHERE advertise.active = 1 and advertise.advertise_template_id in (1, 2, 7) and advertise.end_issue >= {issue} 
        GROUP BY advertise.id
        ORDER BY case when services.id = 4 then 0 when services.id = 6 then 1 else 3 end, advertise.id DESC""")
    pclassy = []
    sclassy = []
    for cl in classys:
        if cl[6]:
            pclassy.append(cl)
        else:
            sclassy.append(cl)
    classys = pclassy + sclassy
    base_context = {
        'categories': categories,
        'classys': classys,
        'lang': lang
    }
    context = {}

    if path.replace('/', '') == 'news':
        template = 'main/index.html'
        context.update(base_context)
        return render(request, template, context)
    else:
        template = 'main/index.html'
        context.update(base_context)
        return render(request, template, context)
