# Generated by Django 3.2 on 2021-04-15 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beer_name', models.CharField(max_length=255)),
                ('sort', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='beers', to='shop.sort')),
            ],
        ),
    ]