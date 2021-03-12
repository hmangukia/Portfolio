# Generated by Django 3.1.7 on 2021-03-05 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210304_1559'),
    ]

    operations = [
        migrations.CreateModel(
            name='Connect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon_code', models.TextField()),
                ('content', models.TextField()),
                ('link', models.URLField(max_length=400)),
                ('username', models.CharField(max_length=200)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='project',
            options={},
        ),
    ]
