# Generated by Django 4.1 on 2022-08-26 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacations', '0007_remove_vacationrequest_emp_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacationrequest',
            name='emp_email',
            field=models.EmailField(max_length=254),
        ),
    ]
