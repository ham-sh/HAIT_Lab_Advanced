# Generated by Django 3.1.2 on 2020-10-19 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20201019_0853'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='email',
        ),
        migrations.RemoveField(
            model_name='student',
            name='grade',
        ),
        migrations.RemoveField(
            model_name='student',
            name='school_name',
        ),
    ]
