# Generated by Django 5.1 on 2024-09-21 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('performer', models.CharField(max_length=100)),
                ('chart_debut', models.CharField(max_length=500)),
                ('peak_position', models.IntegerField()),
                ('time_on_chart', models.IntegerField()),
            ],
        ),
    ]