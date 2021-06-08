from django.http import HttpResponse

def saludo(resquest): #mi primera vista
    return HttpResponse('Hola profe, aquí presentando nuestra primera web desde el framework de Django y subiendolo a GitHub')