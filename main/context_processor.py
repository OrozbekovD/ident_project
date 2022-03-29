from main.models import *

def base(request):

    phones = Phone.objects.all()
    email = Email.objects.all()

    places = Place.objects.first()
    social = Social.objects.all()
    footer = Footer.objects.first()
    catalog = Catalog.objects.all()
    params = {'phones': phones, 'email': email,
              'places': places, 'social': social, 'footer': footer, 'catalog': catalog}
    return params