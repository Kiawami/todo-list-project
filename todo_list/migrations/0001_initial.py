# Generated by Django 4.0.6 on 2022-07-11 11:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=300)),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('deadline', models.DateTimeField(blank=True, null=True)),
                ('is_done', models.BooleanField()),
                ('tags', models.ManyToManyField(to='todo_list.tag')),
            ],
        ),
    ]
