# Generated by Django 3.2.11 on 2022-01-04 20:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Homework",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("text", models.TextField()),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("deadline", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=25)),
                ("last_name", models.CharField(max_length=25)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Teacher",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=25)),
                ("last_name", models.CharField(max_length=25)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="HomeworkResult",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("solution", models.TextField()),
                ("author", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="learning_data.student")),
                (
                    "created",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="learning_data.homework"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="HomeworkDone",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "homework_result",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="learning_data.homeworkresult"),
                ),
            ],
        ),
    ]