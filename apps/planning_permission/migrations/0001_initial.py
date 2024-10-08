# Generated by Django 5.1.1 on 2024-09-18 08:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlanningPermissionCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('category', models.CharField(choices=[('universal', 'Universal category'), ('other', 'Other categories')], max_length=10)),
                ('requires_permission', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Restriction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('planning_codes', models.ManyToManyField(related_name='details', to='planning_permission.planningpermissioncode')),
                ('restriction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='planning_permission.restriction')),
            ],
        ),
    ]
