# Generated by Django 4.2 on 2023-05-09 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0002_remove_user_is_customer_remove_user_is_employee_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='category',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='user',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.AddField(
            model_name='profile',
            name='skill',
            field=models.CharField(default='None', max_length=200),
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Skill',
        ),
    ]
