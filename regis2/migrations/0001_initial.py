# Generated by Django 5.1 on 2024-11-10 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('description', models.CharField(max_length=100, verbose_name='description0')),
                ('value', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='value0')),
                ('paid', models.BooleanField(default=False, verbose_name='paid0')),
            ],
            options={
                'ordering': ('description',),
            },
        ),
    ]
