# Generated by Django 4.0.4 on 2022-05-30 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('idd', models.AutoField(db_column='IdD', primary_key=True, serialize=False)),
                ('issuing_date', models.DateField(blank=True, null=True)),
                ('valid_date', models.DateField(blank=True, null=True)),
                ('issuing_place', models.CharField(blank=True, max_length=50, null=True)),
                ('reg_number', models.CharField(blank=True, max_length=20, null=True)),
                ('image1', models.CharField(blank=True, max_length=50, null=True)),
                ('image2', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'document',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('idu', models.AutoField(db_column='IdU', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(blank=True, max_length=50, null=True)),
                ('avatar', models.CharField(blank=True, max_length=50, null=True)),
                ('email_verified', models.IntegerField(blank=True, null=True)),
                ('token', models.CharField(blank=True, max_length=50, null=True)),
                ('tel', models.CharField(blank=True, max_length=20, null=True)),
                ('bio', models.CharField(blank=True, max_length=256, null=True)),
                ('username', models.CharField(max_length=20)),
                ('doc_verified', models.IntegerField(blank=True, null=True)),
                ('idd', models.ForeignKey(blank=True, db_column='IdD', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.document')),
            ],
            options={
                'db_table': 'user',
                'managed': True,
            },
        ),
    ]
