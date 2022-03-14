from main.models import *

def base(request):

    phones = Phones.objects.all()
    email = Email.objects.all()

    places = Place.objects.first()
    social = Social.objects.all()
    footer = Footer.objects.first()

    params = {'phones': phones, 'email': email,
              'places': places, 'social': social, 'footer': footer}
    return params