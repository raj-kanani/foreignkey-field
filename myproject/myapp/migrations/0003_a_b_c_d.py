# Generated by Django 4.0.4 on 2022-06-02 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_student_school'),
    ]

    operations = [
        migrations.CreateModel(
            name='A',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='B',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='C',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='D',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('a', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.a')),
                ('b', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.b')),
                ('c', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.c')),
            ],
        ),
    ]
