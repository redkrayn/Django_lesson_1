from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_rename_description_long_place_long_description_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='place',
            unique_together={('title', 'short_description')},
        ),
    ]
