from django.shortcuts import render
from django.views import View
from .models import Cliente, Componente, Productos,  Pedido
from django.http import JsonResponse

class ClienteListView(View):
    def get(self, request):
        clientelist = Cliente.objects.all()
        return JsonResponse(list(clientelist.values()), safe=False)

    #def post(self, request):
        # POST...

    #def put(self, request):
        # PUT...

    #def delete(self, request):
        # DELETE...


class ClienteDetailView(View):
    def get(self, request):
        list = Cliente.objects.get(pk=id)
        return JsonResponse(list, safe=False)

    #def post(self, request):
        # POST...

    #def put(self, request):
        # PUT...

    #def delete(self, request):
        # DELETE...
