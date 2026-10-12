from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("dashboard", "0004_appclock"),
    ]

    operations = [
        migrations.CreateModel(
            name="ImageDailyUsage",
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
                ("usage_date", models.DateField()),
                ("successful_count", models.PositiveSmallIntegerField(default=0)),
                ("pending_count", models.PositiveSmallIntegerField(default=0)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="image_daily_usage",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="imagedailyusage",
            constraint=models.UniqueConstraint(
                fields=("user", "usage_date"),
                name="unique_image_usage_per_user_day",
            ),
        ),
    ]
