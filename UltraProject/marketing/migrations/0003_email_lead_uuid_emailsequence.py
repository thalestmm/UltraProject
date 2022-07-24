# Generated by Django 4.0.6 on 2022-07-24 13:34

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0002_leadlabel_associated_image_alter_lead_label'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('message', models.CharField(max_length=1000)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('label', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='marketing.leadlabel')),
            ],
        ),
        migrations.AddField(
            model_name='lead',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.CreateModel(
            name='EmailSequence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours_between_emails', models.IntegerField()),
                ('emails', models.ManyToManyField(to='marketing.email')),
                ('label', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='marketing.leadlabel')),
            ],
        ),
    ]
