from main.models import *

def base(request):

    phones = Phones.objects.all()
    email = Email.objects.all()

    places = Place.objects.first()

    params = {'phones': phones, 'email': email,
              'places': places}
    return params