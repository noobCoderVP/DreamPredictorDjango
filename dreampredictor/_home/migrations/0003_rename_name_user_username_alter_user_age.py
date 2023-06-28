# Generated by Django 4.2 on 2023-04-30 12:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('_home', '0002_user_delete_member'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='username',
        ),
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(12)]),
        ),
    ]
