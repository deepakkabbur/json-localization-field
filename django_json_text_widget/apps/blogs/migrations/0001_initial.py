# Generated by Django 4.1.6 on 2023-02-09 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Article",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.JSONField(default=dict, verbose_name="Article title")),
            ],
            options={
                "verbose_name": "article",
                "verbose_name_plural": "articles",
            },
        ),
    ]