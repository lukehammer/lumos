from django.db import models

class Trick(models.Model):
    name = models.CharField(max_length=128)
    audiences = models.CharField(max_length=128)
    props = models.CharField(max_length=128)
    patter = models.TextField(blank = True)
    cost_to_preform = models.DecimalField(max_digits= 5, decimal_places=2)
    cost_to_buy_effect = models.DecimalField(max_digits= 5, decimal_places=2)
    def __unicode__(self):
        return self.name



class Show(models.Model):
    #address break down in different model
    #day of point of contact
    show_name = models.CharField(max_length=128)
    notes = models.TextField(blank = True)
    tricks = models.ManyToManyField(Trick)
    def __unicode__(self):
        return self.show_name


class Person(models.Model):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    phone_number = models.CharField(max_length=15)
    def __unicode__(self):
        return self.first_name




