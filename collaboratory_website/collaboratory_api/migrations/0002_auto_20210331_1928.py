# Generated by Django 3.1.7 on 2021-03-31 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collaboratory_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='organization_id',
            field=models.ForeignKey(blank=True, db_column='OrganizationID', default='N/A', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='org', to='collaboratory_api.organization'),
        ),
    ]