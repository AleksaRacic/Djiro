# Generated by Django 4.0.4 on 2022-06-02 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0003_alter_ratingdriver_idu_alter_reservation_idu'),
    ]

    operations = [
        migrations.AddField(
            model_name='holding',
            name='date_from',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='holding',
            name='date_to',
            field=models.DateField(blank=True, null=True),
        ),
    ]
