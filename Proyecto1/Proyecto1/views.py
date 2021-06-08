from django.http import HttpResponse

def saludo(request): # mi primera vista

    return HttpResponse("Hola profe, aquí presentando nuestra primera vista creada con el framework de Django y subiendolo a GitHub")