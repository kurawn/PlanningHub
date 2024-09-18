from django.db import models


class PlanningPermissionCode(models.Model):
    CATEGORY_CHOICES = [
        ('universal', 'Universal category'),
        ('other', 'Other categories'),
    ]

    code = models.CharField(max_length=10, unique=True)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    requires_permission = models.BooleanField(default=False)

    def __str__(self):
        category_label = 'Universal' if self.category == 'universal' else 'Other'
        return f"{self.code} - {category_label}: {'Requires Permission' if self.requires_permission else 'No Permission Required'}"
