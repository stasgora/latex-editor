# Generated by Django 3.0.6 on 2020-06-08 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editor_app', '0004_auto_20200608_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formula',
            name='text',
            field=models.TextField(verbose_name='Wyrażenie matematyczna w języku LaTeX'),
        ),
    ]
