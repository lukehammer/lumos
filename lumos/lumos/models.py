from django.db import models

class Shows(models.Model):
    #address break down in different model
    #day of point of contact
    directions_from_parking_to_stage = models.CharField(max_length=200)
    parking = models.CharField(max_length=200)
    loading_unloading_parking = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name

class Tricks(models.Model):
    shows = models.ForeignKey(Shows)
    audiences = models.CharField(max_length=128)
    props = models.CharField(max_length=128)
    patter = models.CharField(max_length=1000)
    cost_to_preform = models.DecimalField(max_digits= 5, decimal_places=2)

    def __unicode__(self):
        return self.title




