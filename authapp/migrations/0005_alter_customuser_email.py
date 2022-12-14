# Generated by Django 3.2.16 on 2022-11-30 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_alter_customuser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(error_messages={'unique': 'A user with that email address already exists.'}, max_length=256, null=True, unique=True, verbose_name='email address'),
        ),
    ]
