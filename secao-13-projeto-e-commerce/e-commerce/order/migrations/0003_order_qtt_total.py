# Generated by Django 5.0.4 on 2024-05-06 21:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0002_alter_orderitem_quantity"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="qtt_total",
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
