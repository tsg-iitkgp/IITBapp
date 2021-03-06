# Generated by Django 2.0.2 on 2018-02-21 11:48

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('events', '0006_usereventstatus_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='followers',
            field=models.ManyToManyField(blank=True, through='events.UserEventStatus', to='users.UserProfile'),
        ),
        migrations.AddField(
            model_name='usereventstatus',
            name='user',
            field=models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, to='users.UserProfile'),
        ),
        migrations.AlterField(
            model_name='event',
            name='image_url',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='usereventstatus',
            name='event',
            field=models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, to='events.Event'),
        ),
    ]
