# Generated by Django 4.2 on 2023-05-03 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_table_id_alter_table_id_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Table',
        ),
    ]
