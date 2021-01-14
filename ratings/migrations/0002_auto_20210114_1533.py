# Generated by Django 3.1.5 on 2021-01-14 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sounds', '0001_initial'),
        ('subjects', '0001_initial'),
        ('ratings', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together={('subject', 'run', 'emotional')},
        ),
    ]