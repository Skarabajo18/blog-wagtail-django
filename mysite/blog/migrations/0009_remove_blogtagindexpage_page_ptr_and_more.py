# Generated by Django 4.1.8 on 2023-04-26 20:31

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0008_blogindexpage"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="blogtagindexpage",
            name="page_ptr",
        ),
        migrations.RemoveField(
            model_name="blogpage",
            name="tags",
        ),
        migrations.DeleteModel(
            name="BlogPageTag",
        ),
        migrations.DeleteModel(
            name="BlogTagIndexPage",
        ),
    ]