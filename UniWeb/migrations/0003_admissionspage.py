# Generated by Django 5.1.1 on 2024-12-18 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UniWeb', '0002_carouselimage_infocolumn_mainpagecontent'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdmissionsPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=750)),
                ('muted_text', models.CharField(max_length=150)),
            ],
        ),
    ]
