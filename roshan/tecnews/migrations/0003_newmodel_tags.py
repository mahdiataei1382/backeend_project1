# Generated by Django 4.2.3 on 2023-07-29 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tecnews', '0002_remove_newmodel_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='newmodel',
            name='Tags',
            field=models.ManyToManyField(to='tecnews.tagmodel'),
        ),
    ]