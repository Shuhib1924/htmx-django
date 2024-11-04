from django.db import models


class Book(models.Model):

    title = models.CharField(db_column="title", max_length=100, blank=False)
    status = models.CharField(db_column="status", max_length=50, blank=False)
    author = models.CharField(
        db_column="author", max_length=100, blank=False, null=False
    )
    year = models.IntegerField(db_column="year", blank=False, default=0)

    class Meta:
        db_table = "book"
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
