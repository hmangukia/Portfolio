# Generated by Django 3.1.7 on 2021-03-05 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210305_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='connect',
            name='social',
            field=models.CharField(default=0, max_length=200, unique=True),
            preserve_default=False,
        ),
    ]
