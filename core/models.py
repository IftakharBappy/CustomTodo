from django.db import models


class Todo(models.Model):

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    created = models.DateTimeField()

    def __unicode__(
            self):
        return self.name



