# Generated by Django 2.1.2 on 2018-10-14 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20181014_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='app_deadline',
            field=models.CharField(default='october', max_length=50),
            preserve_default=False,
        ),
    ]
