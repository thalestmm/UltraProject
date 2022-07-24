from django.db import models
import uuid

# Create your models here.


class LeadLabel(models.Model):
    name = models.CharField(max_length=100, default="lead")
    associated_image = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


# TODO: WHEN SENDING EMAILS, MAKE SURE TO SEND ONLY ONE MAIL PER LABEL/EMAIL PAIR
class Lead(models.Model):
    fname = models.CharField(max_length=20)
    email = models.EmailField()
    label = models.ForeignKey(LeadLabel, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.label) + " / " + str(self.email)


class Email(models.Model):
    message = models.CharField(max_length=1000)
    label = models.ForeignKey(LeadLabel, on_delete=models.SET_NULL, null=True, blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return str(self.label) + " / " + str(self.id)


# TODO: FIND A WAY TO ESTABLISH ORDER FOR EVERY EMAIL - JSON FIELDS?
class EmailSequence(models.Model):
    emails = models.ManyToManyField(Email)
    hours_between_emails = models.IntegerField()
    label = models.ForeignKey(LeadLabel, on_delete=models.SET_NULL, null=True, blank=True)