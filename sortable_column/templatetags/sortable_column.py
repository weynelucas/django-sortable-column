from django import template
from urllib.parse import urlparse, urlunparse
from sortable_column.services.url_service import remove_params, append_params
from django.conf import settings

register = template.Library()

@register.inclusion_tag('sortable_column/sortable_column.html')
def sortable_column(property, title, request, style=None, default_order='asc'):
    full_path = request.get_full_path()
    cleaned_path = remove_params(full_path, ['sort', 'order'])
    conf = __get_settings()

    if request.method == 'POST':
        params = request.POST.copy()
    else:
        params = request.GET.copy()

    orders = ['asc', 'desc']
    if default_order in orders:
        order = default_order
        if default_order == 'desc':
            orders.reverse()
    else:
        order = 'asc'

    sort = params.get('sort')
    sort_icon_suffix = ''
    if sort == property:
        order =  params.get('order', 'asc')
        if order not in orders:
            order = default_order
        sort_icon_suffix = '-'  + order
        order = orders[(orders.index(order)+1)%len(orders)]

    icon = conf['icon' + sort_icon_suffix]
    is_image = icon.endswith(tuple(['.jpg', '.png', '.gif', '.bmp']))

    path = append_params(cleaned_path, {'sort':property, 'order':order})

    context = {
        'title': title,
        'class_name': conf['class-name'],
        'icon': conf['icon' + sort_icon_suffix],
        'is_image': is_image,
        'icon_placement': conf['icon-placement'],
        'style': style,
        'path': path,
    }

    return context


def __get_settings():
    default_conf = __get_default_settings()
    settings_opt = __get_settings_options()
    try:
        conf = settings.SORTABLE_COLUMN_SETTINGS
        settings_attrs = [key for key, value in default_conf.items()]
        for attr in settings_attrs:
            if conf.get(attr) and settings_opt.get(attr) and (conf.get(attr) not in settings_opt.get(attr)):
                conf[attr] = default_conf[attr]
            else:
                conf[attr] = conf.get(attr, default_conf[attr])
    except Exception:
        conf = default_conf
    finally:
        return conf;


def __get_default_settings():
    return {
        'class-name': 'sortable',
        'icon': '',
        'icon-asc':'',
        'icon-desc':'',
        'icon-placement': 'left',
    }

def __get_settings_options():
    return {
        'icon-placement': ['left', 'rigth'],
    }
