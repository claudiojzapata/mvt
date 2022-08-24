from django.shortcuts import render, HttpResponse
from django.template import loader #aca importamos el cargador
from familiares.models import familiar
# Create your views here.
#definimos vistas utilizando funciones

def integrantes(request):
    integrante_1 = familiar(nombre = 'Rocio', edad = '20', parentesco = 'Hija')
    integrante_1.save()

    integrante_2 = familiar(nombre = 'Mateo', edad = '9', parentesco = 'Sobrino')
    integrante_2.save()

    integrante_3 = familiar(nombre = 'Martin', edad = '7', parentesco = 'Sobrino')
    integrante_3.save()

    integrante_4 = familiar(nombre = 'Marcos', edad = '12', parentesco = 'Sobrino')
    integrante_4.save()

    plantilla = loader.get_template('parteFlia.html'),
    familiares = {'familiares':[integrante_1, integrante_2, integrante_3, integrante_4]}

    documento = plantilla.render(familiares)

    return HttpResponse(documento)
    

