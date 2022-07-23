from django.db import models

# Create your models here.


class LeadLabel(models.Model):
    name = models.CharField(max_length=100, default="lead")

    def __str__(self):
        return self.name


class Lead(models.Model):
    fname = models.CharField(max_length=20)
    email = models.EmailField()
    label = models.ForeignKey(LeadLabel, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.email