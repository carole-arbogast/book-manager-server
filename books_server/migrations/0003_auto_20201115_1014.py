# Generated by Django 3.1.3 on 2020-11-15 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_server', '0002_remove_bookshelf_books'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='bookshelves',
        ),
        migrations.AddField(
            model_name='bookshelf',
            name='book',
            field=models.ManyToManyField(related_name='books', to='books_server.Book'),
        ),
    ]
