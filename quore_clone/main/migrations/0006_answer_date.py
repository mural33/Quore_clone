# Generated by Django 4.2.1 on 2023-05-25 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_answer_user_alter_question_user_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
