# Generated by Django 5.0.4 on 2024-05-17 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0012_rename_borrowed_books_borrowingrecord_borrowed_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(default='book_covers\\default.png', upload_to='book_covers\\'),
        ),
    ]