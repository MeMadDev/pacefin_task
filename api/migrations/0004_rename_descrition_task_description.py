# Generated by Django 4.2.3 on 2023-12-21 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_task_delete_item'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='descrition',
            new_name='description',
        ),
    ]
