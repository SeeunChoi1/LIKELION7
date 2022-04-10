# Generated by Django 2.2 on 2019-04-10 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0005_auto_20190410_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='star_rate',
            field=models.IntegerField(choices=[(5, '5'), (4, '4'), (3, '3'), (2, '2'), (1, '1'), (0, '0')], default=0, max_length=3),
        ),
    ]