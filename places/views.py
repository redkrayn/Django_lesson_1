from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Place


def show_point(request):
    places = Place.objects.all()
    features_point = []

    for place in places:
        features = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.lng, place.lat]
            },
            'properties': {
                'title': place.title,
                'placeId': place.id,
                'detailsUrl': reverse('place', args=[place.id])
            }
        }
        features_point.append(features)

    points = {
        'type': 'FeatureCollection',
        'features': features_point
    }
    data = {'points': points}

    return render(request, 'index.html', context=data)


def show_place(request, id):
    place = get_object_or_404(Place.objects.prefetch_related('images'), pk=id)

    images = place.images.all()
    urls = [image.image.url for image in images]
    place_info = {
        'title': place.title,
        'description_short': place.short_description,
        'description_long': place.long_description,
        'coordinates': [place.lng, place.lat],
        'imgs': urls,
    }

    return JsonResponse(place_info, safe=False, json_dumps_params={'ensure_ascii': False})
