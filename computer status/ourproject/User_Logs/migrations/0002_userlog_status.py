# Generated by Django 5.2 on 2025-05-14 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_Logs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlog',
            name='status',
            field=models.CharField(choices=[('Using', 'Currently Using'), ('Used', 'Used'), ('Booked', 'Booked')], default='Booked', max_length=10),
        ),
    ]
