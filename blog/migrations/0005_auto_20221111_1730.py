# Generated by Django 3.2.16 on 2022-11-11 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_profile_profilepic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profilePic',
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='default_profile_picture.jpg', upload_to='images/profile'),
        ),
    ]
