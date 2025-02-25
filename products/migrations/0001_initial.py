# Generated by Django 5.1 on 2024-08-28 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('available', 'Available'), ('reserved', 'Reserved'), ('unavailable', 'Unavailable')], default='available', max_length=15)),
            ],
        ),
    ]
