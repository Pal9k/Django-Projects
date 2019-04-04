# Generated by Django 2.1.5 on 2019-04-03 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InfoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='PPTModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ppt', models.ImageField(blank=True, upload_to='images/PPT_Gallary/', verbose_name='PPT')),
                ('user', models.ForeignKey(default=None, on_delete=None, to='PPT_Gallary.InfoModel')),
            ],
        ),
    ]
