# Generated by Django 4.0.4 on 2022-05-10 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='message',
            field=models.CharField(max_length=280),
        ),
    ]
