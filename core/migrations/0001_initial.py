
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uu_id', models.UUIDField(default=uuid.uuid4)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('release_date', models.DateField()),
                ('genre', models.CharField(choices=[('action', 'Action'), ('comedy', 'Comedy'), ('drama', 'Drama'), ('horror', 'Horror'), ('romance', 'Romance'), ('science_fiction', 'Science Fiction'), ('fantasy', 'Fantasy')], max_length=100)),
                ('length', models.PositiveIntegerField()),
                ('image_card', models.ImageField(upload_to='movie_images/')),
                ('image_cover', models.ImageField(upload_to='movie_images/')),
                ('video', models.FileField(upload_to='movie_videos/')),
                ('movie_views', models.IntegerField(default=0)),
            ],
        ),
    ]
