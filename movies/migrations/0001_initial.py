# Generated by Django 3.1.3 on 2020-12-07 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('actors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('length', models.CharField(max_length=200)),
                ('actors', models.ManyToManyField(blank=True, to='actors.Actor')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Commercial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('company', models.CharField(max_length=200)),
                ('actors', models.ManyToManyField(blank=True, to='actors.Actor')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
