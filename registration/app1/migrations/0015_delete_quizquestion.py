# Generated by Django 3.2.24 on 2024-03-29 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0014_questions_quizlevel_quizquestion'),
    ]

    operations = [
        migrations.DeleteModel(
            name='QuizQuestion',
        ),
    ]
