from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return "%s - %s" % (self.id, self.name)
