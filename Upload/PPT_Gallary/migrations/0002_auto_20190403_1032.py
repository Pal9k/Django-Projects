# Generated by Django 2.1.5 on 2019-04-03 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PPT_Gallary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pptmodel',
            name='ppt',
            field=models.FileField(blank=True, upload_to='images/PPT_Gallary/', verbose_name='PPT'),
        ),
    ]
