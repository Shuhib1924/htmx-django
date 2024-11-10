from django.db import models


class TimeStampedModel(models.Model):
    created = models.DateTimeField("created", auto_now_add=True, auto_now=False)
    modified = models.DateTimeField("modified", auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True


class Expense(TimeStampedModel):
    description = models.CharField("description0", max_length=100)
    value = models.DecimalField("value0", max_digits=10, decimal_places=2)
    paid = models.BooleanField("paid0", default=False)

    class Meta:
        ordering = ("description",)

    def __str__(self):
        return self.description
