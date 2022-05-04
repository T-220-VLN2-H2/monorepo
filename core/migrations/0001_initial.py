# Generated by Django 4.0.4 on 2022-05-04 14:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Catagory",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=128)),
            ],
            options={
                "db_table": "core_catagory",
            },
        ),
        migrations.CreateModel(
            name="Item",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "condition",
                    models.CharField(
                        choices=[
                            ("NEW", ""),
                            ("USED", ""),
                            ("USED_LIKE_NEW", ""),
                            ("FOR_PARTS", "For parts: not working"),
                        ],
                        max_length=128,
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.catagory"
                    ),
                ),
            ],
            options={
                "db_table": "core_item",
            },
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                "db_table": "core_order",
            },
        ),
        migrations.CreateModel(
            name="PaymentInfo",
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
                ("cardholder_name", models.CharField(max_length=128)),
                ("card_number", models.CharField(max_length=16)),
                ("cvc", models.CharField(max_length=3)),
                ("expiry_month", models.IntegerField()),
                ("expiry_year", models.IntegerField()),
            ],
            options={
                "db_table": "core_payment_info",
            },
        ),
        migrations.CreateModel(
            name="RatingUsers",
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
                (
                    "type",
                    models.CharField(
                        choices=[("Rater", ""), ("Ratee", "")], max_length=128
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ShippingDetails",
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
                ("full_name", models.CharField(max_length=128)),
                ("address", models.CharField(max_length=128)),
                ("postal_code", models.SmallIntegerField()),
                ("city", models.CharField(max_length=128)),
            ],
            options={
                "db_table": "core_shipping_details",
            },
        ),
        migrations.CreateModel(
            name="UserSales",
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
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "core_user_sales",
            },
        ),
        migrations.CreateModel(
            name="UserRatings",
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
                ("rating", models.DecimalField(decimal_places=0, max_digits=1)),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.order"
                    ),
                ),
                (
                    "users",
                    models.ManyToManyField(
                        through="core.RatingUsers", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
            options={
                "db_table": "core_user_ratings",
            },
        ),
        migrations.CreateModel(
            name="UserProfile",
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
                ("description", models.TextField(blank=True, max_length=500)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "core_user",
            },
        ),
        migrations.CreateModel(
            name="UserBids",
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
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("expires", models.DateTimeField()),
                (
                    "item_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.item"
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "core_user_bids",
            },
        ),
        migrations.CreateModel(
            name="SearchHistory",
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
                ("search_string", models.CharField(max_length=128)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "core_search_history",
            },
        ),
        migrations.AddField(
            model_name="ratingusers",
            name="user_rating",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="core.userratings"
            ),
        ),
        migrations.CreateModel(
            name="OrderUser",
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
                (
                    "type",
                    models.CharField(
                        choices=[("Buyer", ""), ("Seller", "")], max_length=128
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.order"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OrderItems",
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
                (
                    "order_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.order"
                    ),
                ),
            ],
            options={
                "db_table": "core_order_items",
            },
        ),
        migrations.CreateModel(
            name="OrderHistory",
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
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "core_order_history",
            },
        ),
        migrations.AddField(
            model_name="order",
            name="users",
            field=models.ManyToManyField(
                through="core.OrderUser", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
