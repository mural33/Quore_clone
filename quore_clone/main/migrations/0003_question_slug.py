# Generated by Django 4.2.1 on 2023-05-24 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_question_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='slug',
            field=models.SlugField(default='', max_length=1000),
        ),
    ]
