from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context


def hello_world(request):
    return HttpResponse("Hello, world. You're at the Django - CoderHouse first view.")

def segunda_vista(request):
    return HttpResponse("<br>Ya entendimos esto, es muy simple :)<br>")

def diaDeHoy(request):

        dia = datetime.now()    

        documentoDeTexto = f"Hoy es día: <br> {dia}"


        return HttpResponse(documentoDeTexto)

def miNombreEs(self, nombre):

      documentoDeTexto = f"Mi nombre es: <br><br>  {nombre}"


      return HttpResponse(documentoDeTexto)

def probandoTemplate(self):

    miHtml = open("C:/Users/juanp/coderhouse/class_16_git/live_class/live_class/mysite/mysite/templates/template.html")

    plantilla = Template(miHtml.read()) #Se carga en memoria nuestro documento, template1   
    ##OJO importar template y contex, con: from django.template import Template, Context

    miHtml.close() #Cerramos el archivo

    miContexto = Context() #EN este caso no hay nada ya que no hay parametros, IGUAL hay que crearlo

    documento = plantilla.render(miContexto) #Aca renderizamos la plantilla en documento

    return HttpResponse(documento)
