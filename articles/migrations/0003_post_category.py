# Generated by Django 3.1.4 on 2021-01-30 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[(1, 'Arduino'), (2, 'Robotics'), (3, 'Articles')], default=1, max_length=255),
            preserve_default=False,
        ),
    ]
