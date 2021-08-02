# Generated by Django 3.2.5 on 2021-07-09 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Code', models.CharField(max_length=30)),
                ('Name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Programs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('General_hours', models.IntegerField()),
                ('Code', models.IntegerField()),
                ('Classroom_hours', models.IntegerField()),
                ('Registration_date', models.DateTimeField(auto_now_add=True)),
                ('Type', models.CharField(max_length=20)),
                ('Dep', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='program.departments')),
            ],
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Code', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Mod',
        ),
        migrations.AddField(
            model_name='programs',
            name='Specialty',
            field=models.ManyToManyField(to='program.Specialty'),
        ),
        migrations.AddField(
            model_name='direction',
            name='Spec',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='program.specialty'),
        ),
    ]