from django.shortcuts import render
from main.models import Categories, Advertise, Settings
from google_trans_new import google_translator


def index(request, path):
    translator = google_translator()
    issue = int(Settings.objects.filter(id=1).values('svalue')[0]['svalue'])
    tClassies = Advertise.objects.filter(active=1, advertise_template_id__in=[1, 2, 7], end_issue__gte=issue, newspaper_content_en=None).order_by(
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
    classys = list(Advertise.objects.filter(active=1, advertise_template_id__in=[1, 2, 7], end_issue__gte=issue).order_by(
            '-id').values())
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
