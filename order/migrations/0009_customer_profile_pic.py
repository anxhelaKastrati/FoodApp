# Generated by Django 3.2.5 on 2021-07-14 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_menuitem_item_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile1.png', null=True, upload_to=''),
        ),
    ]
