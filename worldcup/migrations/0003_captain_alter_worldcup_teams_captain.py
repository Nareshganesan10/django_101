# Generated by Django 4.1 on 2023-01-16 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("worldcup", "0002_alter_worldcup_teams_goals"),
    ]

    operations = [
        migrations.CreateModel(
            name="Captain",
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
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("club", models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name="worldcup_teams",
            name="captain",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="worldcup.captain"
            ),
        ),
    ]
