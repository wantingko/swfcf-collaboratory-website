# Generated by Django 3.1.7 on 2021-03-20 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collaboratory_api', '0011_auto_20210320_0014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='id',
        ),
        migrations.AlterField(
            model_name='organization',
            name='ein',
            field=models.IntegerField(db_column='EIN', primary_key=True, serialize=False),
        ),
    ]
