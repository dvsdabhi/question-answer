# Generated by Django 5.2.1 on 2025-06-03 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('category', models.CharField(choices=[('resume', 'Resume Tip'), ('interview', 'Interview Tip')], max_length=100)),
            ],
        ),
    ]
