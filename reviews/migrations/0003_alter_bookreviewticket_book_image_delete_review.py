# Generated by Django 4.2.5 on 2023-10-09 14:19

from django.db import migrations, models
import reviews.models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_bookreviewticket_bookreview_alter_review_ticket_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookreviewticket',
            name='book_image',
            field=models.ImageField(upload_to=reviews.models.book_image_path),
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]
