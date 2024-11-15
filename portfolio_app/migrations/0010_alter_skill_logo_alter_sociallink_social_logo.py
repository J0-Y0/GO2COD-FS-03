# Generated by Django 5.1.1 on 2024-11-14 21:59

import portfolio_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0009_alter_skill_description_alter_skill_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='logo',
            field=models.FileField(blank=True, null=True, upload_to='skill_logos/', validators=[portfolio_app.models.validate_image_file]),
        ),
        migrations.AlterField(
            model_name='sociallink',
            name='social_logo',
            field=models.FileField(upload_to='social_logos/', validators=[portfolio_app.models.validate_image_file]),
        ),
    ]