# Generated by Django 4.1 on 2023-03-16 01:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("maths", "0004_result_maths_result_value_error_together"),
    ]

    operations = [
        migrations.AddField(
            model_name="math",
            name="result",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="maths.result",
            ),
        ),
    ]
