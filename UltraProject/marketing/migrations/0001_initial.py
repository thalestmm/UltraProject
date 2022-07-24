# Generated by Django 4.0.6 on 2022-07-23 01:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LeadLabel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='lead', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('label', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='marketing.leadlabel')),
            ],
        ),
    ]