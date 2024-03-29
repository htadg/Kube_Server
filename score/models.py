from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class LeaderBoard(models.Model):
    name = models.CharField(_("Name"), max_length=50, blank=True, default="Anonymous")
    score = models.IntegerField(_("Score"), blank=False)

    def __str__(self):
        return "%s" % self.name

    def save(self, *args, **kwargs):
        self.name = str(self.name).upper()
        self.score = int(self.score)
        super(LeaderBoard, self).save(*args, **kwargs)
