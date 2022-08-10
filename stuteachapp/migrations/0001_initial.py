# Generated by Django 4.1 on 2022-08-09 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('rollno', models.IntegerField()),
                ('standard', models.IntegerField()),
                ('stream', models.CharField(max_length=40)),
                ('dateofbirth', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(choices=[('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('Social Science', 'Social Science'), ('Mathematics', 'Mathematics'), ('Biology', 'Biology'), ('Computer', 'Computer'), ('Hindi', 'Hindi'), ('English', 'English')], max_length=20)),
                ('name', models.CharField(max_length=30)),
                ('phonenumber', models.CharField(max_length=10)),
                ('classestaught', models.IntegerField()),
            ],
        ),
    ]