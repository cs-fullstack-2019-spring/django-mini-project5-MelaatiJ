# Generated by Django 2.0.6 on 2019-03-11 17:15

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameOfMeal', models.CharField(default='', max_length=200)),
                ('shortDescription', models.TextField(default='', max_length=200)),
                ('dateCreated', models.DateField(default=datetime.date.today)),
                ('chef', models.CharField(default='', max_length=100)),
                ('ingredients', models.TextField(default='', max_length=800)),
                ('directions', models.TextField(default='', max_length=900)),
                ('recipe_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('username', models.CharField(default='', max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('profilePic', models.CharField(default='', max_length=800)),
                ('password1', models.CharField(default='', max_length=100)),
                ('password2', models.CharField(default='', max_length=100)),
                ('User_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
