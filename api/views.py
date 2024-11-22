from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Usuario

@api_view(['POST'])
def registrar_usuario(request):
    nombre = request.data.get('nombre')
    correo = request.data.get('correo')

    if not nombre or not correo:
        return Response({"success": False, "message": "Nombre y correo son obligatorios."})

    if Usuario.objects.filter(correo=correo).exists():
        return Response({"success": False, "message": "El correo ya está registrado."})

    Usuario.objects.create(nombre=nombre, correo=correo)
    return Response({"success": True, "message": "Usuario registrado exitosamente."})
