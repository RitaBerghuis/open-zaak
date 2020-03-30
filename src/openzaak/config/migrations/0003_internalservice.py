# Generated by Django 2.2.10 on 2020-03-20 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("config", "0002_rename_nlx_inway"),
    ]

    operations = [
        migrations.CreateModel(
            name="InternalService",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "api_type",
                    models.CharField(
                        choices=[
                            ("ac", "Autorisatiecomponent"),
                            ("nrc", "Notificatierouteringcomponent"),
                            ("zrc", "Zaakregistratiecomponent"),
                            ("ztc", "Zaaktypecatalogus"),
                            ("drc", "Documentregistratiecomponent"),
                            ("brc", "Besluitregistratiecomponent"),
                        ],
                        max_length=50,
                        unique=True,
                        verbose_name="API type",
                    ),
                ),
                (
                    "enabled",
                    models.BooleanField(
                        default=True,
                        help_text="Boolean indicates if internal API is enabled",
                        verbose_name="enabled",
                    ),
                ),
                (
                    "nlx",
                    models.BooleanField(
                        default=True,
                        help_text="Boolean indicated if the service is available via NLX inway",
                        verbose_name="nlx",
                    ),
                ),
            ],
            options={
                "verbose_name": "Internal service",
                "verbose_name_plural": "Internal services",
            },
        ),
    ]