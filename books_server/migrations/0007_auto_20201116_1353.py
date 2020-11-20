# Generated by Django 3.1.3 on 2020-11-16 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books_server', '0006_auto_20201115_1021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='bookshelves',
        ),
        migrations.AddField(
            model_name='book',
            name='bookshelves',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='books_server.bookshelf'),
            preserve_default=False,
        ),
    ]