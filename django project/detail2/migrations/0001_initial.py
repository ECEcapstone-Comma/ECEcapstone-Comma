# Generated by Django 3.2.19 on 2023-05-17 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jungi_Audition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planning_agency', models.CharField(max_length=100)),
                ('audition_name', models.CharField(max_length=100)),
                ('recruitment_field', models.CharField(max_length=50)),
                ('age_group1', models.IntegerField()),
                ('age_group2', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('due_date', models.CharField(max_length=20)),
                ('url', models.URLField()),
                ('data_number', models.IntegerField()),
            ],
        ),
    ]
