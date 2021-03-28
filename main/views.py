from django.shortcuts import render

from main.models import Categories, Advertise, Settings


def index(request, path):
    issue = int(Settings.objects.filter(id=1).values('svalue')[0]['svalue'])
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
