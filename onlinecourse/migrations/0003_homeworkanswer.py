# Generated by Django 3.1.3 on 2021-06-23 02:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_auto_20210623_0941'),
    ]

    operations = [
        migrations.CreateModel(
            name='Homeworkanswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choices', models.ManyToManyField(to='onlinecourse.Choice')),
                ('homework', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.homework')),
            ],
        ),
    ]
