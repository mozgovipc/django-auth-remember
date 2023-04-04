# Generated by Django 3.2.16 on 2023-04-04 17:21

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RememberToken',
            fields=[
                ('token_hash', models.CharField(max_length=80, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime.now, editable=False)),
                ('created_initial', models.DateTimeField(editable=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='remember_me_tokens', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
