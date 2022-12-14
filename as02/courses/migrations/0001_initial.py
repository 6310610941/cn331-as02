# Generated by Django 4.1.1 on 2022-09-17 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.IntegerField()),
                ('year', models.IntegerField()),
                ('seat', models.IntegerField()),
                ('status', models.CharField(max_length=64)),
                ('subname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Subject_Name', to='courses.course')),
            ],
        ),
    ]
