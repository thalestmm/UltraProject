# Generated by Django 4.0.6 on 2022-07-25 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_question_exam_name_alter_question_subject'),
        ('marketing', '0002_alter_unsubscribeevent_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='exam',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.exam'),
        ),
    ]