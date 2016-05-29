from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def post_departamentos(request):
	return render(request,'administracion/migrations/post_departamentos.html', {})

def holaMundo(request):
    html = "<html><body>Hola Mundo desde DJANGO</body></html>"
    return HttpResponse(html)

def fecha_actual(request):
    ahora = datetime.datetime.now()
    html = "<html><body><h1>Fecha:</h1><h3>%s<h/3></body></html>" % ahora
    return HttpResponse(html)
