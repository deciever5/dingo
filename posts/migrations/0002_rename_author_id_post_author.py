# Generated by Django 4.1.7 on 2023-03-15 09:07

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="author_id",
            new_name="author",
        ),
    ]
