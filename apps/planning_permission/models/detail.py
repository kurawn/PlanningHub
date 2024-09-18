from django.db import models

from .restriction import Restriction


class Detail(models.Model):
    restriction = models.ForeignKey(Restriction, on_delete=models.CASCADE, related_name='details')
    description = models.CharField(max_length=255)
    planning_codes = models.ManyToManyField('PlanningPermissionCode', related_name='details')

    def __str__(self):
        return f"{self.restriction}: {self.description}"
