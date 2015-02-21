from django.db import models


class Trick(models.Model):
    name = models.CharField(max_length=128, unique=True)
    length = models.DecimalField(max_digits=4, decimal_places=2)


    def __unicode__(self):
        return self.name

class Show(models.Model):
    trick = models.ManyToManyField(Trick)
    title = models.CharField(max_length=128)
    fee = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

# Create your models here.
