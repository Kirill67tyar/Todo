# Generated by Django 3.0.8 on 2020-08-25 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_tagcount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tagcount',
            old_name='tag_clug',
            new_name='tag_slug',
        ),
    ]
