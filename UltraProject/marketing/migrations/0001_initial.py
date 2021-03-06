# Generated by Django 4.0.6 on 2022-07-24 19:06

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('subject', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=1000)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='LeadLabel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='lead', max_length=100)),
                ('associated_image', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UnsubscribeReason',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UnsubscribeEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('reason', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='marketing.unsubscribereason')),
            ],
        ),
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('email_mkt', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('label', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='marketing.leadlabel')),
            ],
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
        migrations.AddField(
            model_name='email',
            name='label',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='marketing.leadlabel'),
        ),
    ]
