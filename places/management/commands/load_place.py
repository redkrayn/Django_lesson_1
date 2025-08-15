from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from places.models import Place
import requests


def get_place_from_json(url):
    response = requests.get(url)
    response.raise_for_status()
    response = response.json()
    place, _ = Place.objects.get_or_create(
        title=response['title'],
        description_short=response['description_short'],
        description_long=response['description_long'],
        lng=response['coordinates']['lng'],
        lat=response['coordinates']['lat']
    )

    for image_number, image in enumerate(response['imgs'], start=0):
        picture = requests.get(image)
        picture.raise_for_status()
        place.images.create(
            image=ContentFile(picture.content, f'{place.title}_{image_number}.jpg'),
            sequence_number=image_number
        )


class Command(BaseCommand):
    help = 'Load places from json'

    def handle(self, *args, **options):
        if options['url']:
            print(options['url'])
            get_place_from_json(options['url'])

    def add_arguments(self, parser):
        parser.add_argument(
            'url',
            nargs='?'
        )
