# Generated by Django 4.1 on 2022-08-26 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacations', '0003_remove_vacationrequest_employee_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacationrequest',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]