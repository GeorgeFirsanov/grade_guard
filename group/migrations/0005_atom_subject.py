# Generated by Django 4.1.7 on 2023-05-14 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0004_professor'),
    ]

    operations = [
        migrations.AddField(
            model_name='atom',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='group.subject'),
        ),
    ]
