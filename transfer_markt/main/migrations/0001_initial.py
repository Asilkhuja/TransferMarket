# Generated by Django 4.2.3 on 2023-07-21 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_cat_name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=50)),
                ('player_age', models.IntegerField()),
                ('player_club', models.CharField(max_length=100)),
                ('player_position', models.CharField(max_length=50)),
                ('contract_per', models.DateTimeField()),
                ('player_price', models.IntegerField()),
                ('added_time', models.DateTimeField(auto_now_add=True)),
                ('player_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.player_category')),
            ],
        ),
    ]
