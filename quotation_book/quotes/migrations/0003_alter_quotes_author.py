# Generated by Django 5.0.1 on 2024-03-03 12:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0002_alter_tag_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotes',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quotes.authors'),
        ),
    ]
