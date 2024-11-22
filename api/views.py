from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Usuario

@api_view(['POST'])
def registrar_usuario(request):
    try:
        nombre = request.data.get('nombre')
        correo = request.data.get('correo')

        if not nombre or not correo:
            return Response({"success": False, "message": "Nombre y correo son obligatorios."}, status=400)

        if Usuario.objects.filter(correo=correo).exists():
            return Response({"success": False, "message": "El correo ya está registrado."}, status=400)

        Usuario.objects.create(nombre=nombre, correo=correo)
        return Response({"success": True, "message": "Usuario registrado exitosamente."})
    except Exception as e:
        return Response({"success": False, "message": f"Error del servidor: {str(e)}"}, status=500)
