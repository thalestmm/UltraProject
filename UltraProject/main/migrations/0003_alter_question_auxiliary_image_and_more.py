# Generated by Django 4.0.6 on 2022-07-22 17:09

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_question_alt_a_question_alt_b_question_alt_c_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='auxiliary_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='question',
            name='difficulty_level',
            field=models.IntegerField(default=3, validators=[main.models.validate_difficulty_range]),
        ),
        migrations.AlterField(
            model_name='question',
            name='solution_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
