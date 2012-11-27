from django.db import models
from mezzanine.core.models import SiteRelated


class Theme(SiteRelated):
    THEME_CHOICES = (('am', 'amelia'),
                     ('ce', 'cerulean'),
                     ('cy','cyborg'),
                     ('jo','journal'),
                     ('pr','project'),
                     ('py','pygments'),
                     ('re','readable'),
                     ('sl','slate'),
                     ('sp','spacelab'),
                     ('spr','spruce'),
                     ('su','superhero'),
                     ('un','united',))

    theme_name = models.CharField(max_length=3,
                                    choices=THEME_CHOICES,
                                    default='amelia')
