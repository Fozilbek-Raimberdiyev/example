# Generated by Django 4.1 on 2022-08-27 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0008_genre_sale_remove_book_image_remove_book_price_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="sale",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.RESTRICT, to="home.sale"
            ),
        ),
        migrations.AlterField(
            model_name="book",
            name="description",
            field=models.TextField(max_length=1000),
        ),
    ]
