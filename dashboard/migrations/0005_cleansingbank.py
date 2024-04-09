# Generated by Django 5.0.1 on 2024-03-18 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_kodebankdummy'),
    ]

    operations = [
        migrations.CreateModel(
            name='CleansingBank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sandi_kliring', models.CharField(max_length=255)),
                ('nama_bank', models.CharField(max_length=255)),
                ('BIC', models.CharField(max_length=255)),
                ('kode_wilayah', models.CharField(max_length=255)),
                ('nama_wilayah', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
