# Generated by Django 4.1 on 2022-11-06 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_alter_book_count_alter_book_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
