# Generated by Django 4.1.3 on 2022-12-12 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='session_key',
            field=models.CharField(default='v3t8tvgajpuphqakbik6p9vj5scn1hrn', max_length=200),
            preserve_default=False,
        ),
    ]
