from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item

@api_view(['GET'])
def lista_items(request):
    items = Item.objects.all().values('id', 'nombre', 'descripcion')
    return Response(list(items))
