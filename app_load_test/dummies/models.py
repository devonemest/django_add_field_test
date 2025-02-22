from django.db import models

class Dummies(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    height = models.FloatField()
    weight = models.FloatField()

    #new_field_test = models.CharField(max_length=100, blank=True, null=True)
    #new_field_test = models.CharField(max_length=100, blank=True, null=True, default ="1")

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'dummies'
