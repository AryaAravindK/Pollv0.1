# Generated by Django 5.0.6 on 2024-07-22 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_response_submit_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mcq',
            name='correct_answer',
            field=models.CharField(max_length=200),
        ),
    ]