# Generated by Django 3.0 on 2022-05-07 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0016_auto_20220409_0618'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.CharField(max_length=30)),
                ('resume', models.CharField(max_length=500)),
            ],
        ),
    ]
