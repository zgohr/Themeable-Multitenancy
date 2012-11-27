from django.core.exceptions import ObjectDoesNotExist
from mezzanine.utils.sites import current_site_id
from models import Theme


def theme(request):
    try:
        t = Theme.objects.get(site=current_site_id())
        return {'theme': t.get_theme_name_display()}
    except ObjectDoesNotExist:
        return {}
