# Generated by Django 4.0.6 on 2022-07-22 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_question_auxiliary_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='auxiliary_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='question',
            name='solution_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
