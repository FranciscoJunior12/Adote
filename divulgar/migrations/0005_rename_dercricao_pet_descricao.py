# Generated by Django 4.1.6 on 2023-02-12 22:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('divulgar', '0004_pet'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='dercricao',
            new_name='descricao',
        ),
    ]
