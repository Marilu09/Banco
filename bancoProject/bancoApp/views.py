import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed

from .models import Costomer, Account

# Create your views here.
def home (request):
    return HttpResponse ("Bienvenido a su banco")

def newCustomer (request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            costomer = Costomer( 
                id = data["id"],
                firstName = data["firstName"],
                lastName = data["lastName"],
                email= data["email"],
                password = data["password"],
            )
            costomer.save()
            return HttpResponse("Nuevo cliente agregado")
        except:
            return HttpResponse("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed (['POST'],"metodo invalido")


def getAllCustomers (request):
    if request.method == 'GET':
        customers = Costomer.objects.all()
        if (not customers):
            return HttpResponse("No hay clientes en la base de datos")
        allCustData = []
        for x in customers:
            data = {"id": x.id, "firstName": x.firstName, "lastName": x.lastName, "email": x.email}
            allCustData.append(data)
        dataJson = json.dumps(allCustData)
        resp = HttpResponse()
        resp.headers['Content-Type'] = "text/json"
        resp.content = dataJson
        return resp
    else:
        return HttpResponseNotAllowed (['GET'],"metodo invalido")


def getOneCustomer (request, id):
    if request.method == 'GET':
        customer = Costomer.objects.filter(id=id).first()
        if (not customer):
            return HttpResponse("No existe cliente con esa cedula")
        data = {"id": customer.id, "firstName": customer.firstName, "lastName": customer.lastName, "email": customer.email}
        dataJson = json.dumps(data)
        resp = HttpResponse()
        resp.headers['Content-Type'] = "text/json"
        resp.content = dataJson
        return resp
    else:
        return HttpResponseNotAllowed (['GET'],"metodo invalido")
