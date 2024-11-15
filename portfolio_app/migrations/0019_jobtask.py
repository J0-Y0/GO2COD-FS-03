# Generated by Django 5.1.1 on 2024-11-15 16:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0018_rename_job_title_experience_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=255)),
                ('experience', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='portfolio_app.experience')),
            ],
        ),
    ]
