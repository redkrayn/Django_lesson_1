import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('description_short', models.TextField(blank=True, verbose_name='Краткое описание')),
                ('description_long', tinymce.models.HTMLField(blank=True, verbose_name='полное описание')),
                ('lat', models.FloatField(verbose_name='Широта')),
                ('lng', models.FloatField(verbose_name='Долгота')),
            ],
        ),
    ]
