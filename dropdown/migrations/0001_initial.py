# Generated by Django 4.1.7 on 2023-02-27 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_actor', models.CharField(max_length=250, verbose_name='Актер')),
            ],
            options={
                'verbose_name': 'Актеры',
                'verbose_name_plural': 'Актер',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True, verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': 'Уроки',
            },
        ),
        migrations.CreateModel(
            name='Prepod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_prepod', models.CharField(max_length=250, verbose_name='Препод')),
            ],
            options={
                'verbose_name': 'Преподы',
                'verbose_name_plural': 'Преподы',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.CharField(max_length=250, verbose_name='Кабинет')),
            ],
            options={
                'verbose_name': 'Кабинет',
                'verbose_name_plural': 'Кабинет',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(default=0, max_length=20, null=True)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dropdown.actor', verbose_name='Актер')),
                ('name_good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dropdown.room', verbose_name='Кабинет')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dropdown.order', verbose_name='ЗАлупа')),
                ('subcat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dropdown.prepod', verbose_name='Препод')),
            ],
        ),
        migrations.CreateModel(
            name='AllowedCombination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dropdown.actor')),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dropdown.room')),
                ('subcat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dropdown.prepod')),
            ],
            options={
                'verbose_name': 'Всевозможные комбинации',
                'verbose_name_plural': 'Всевозможные комбинации',
                'ordering': ['pk'],
            },
        ),
    ]
