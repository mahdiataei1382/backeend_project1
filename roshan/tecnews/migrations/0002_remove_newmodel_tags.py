# Generated by Django 4.2.3 on 2023-07-29 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tecnews', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newmodel',
            name='Tags',
        ),
    ]
