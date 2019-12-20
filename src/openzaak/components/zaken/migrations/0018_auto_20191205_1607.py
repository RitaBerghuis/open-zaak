# Generated by Django 2.2.4 on 2019-12-05 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("besluiten", "0012_auto_20191128_1536"),
        ("zaken", "0017_auto_20191205_1139"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="zaakbesluit",
            options={
                "verbose_name": "zaakbesluit",
                "verbose_name_plural": "zaakbesluiten",
            },
        ),
        migrations.AlterUniqueTogether(
            name="zaakbesluit", unique_together={("zaak", "_besluit")},
        ),
        migrations.AddConstraint(
            model_name="zaakbesluit",
            constraint=models.UniqueConstraint(
                condition=models.Q(_besluit_url="", _negated=True),
                fields=("zaak", "_besluit_url"),
                name="unique_zaak_and_besluit_document",
            ),
        ),
    ]
