from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import BookSerializer,AuthorSerializer, UserSerializer
from .models import Book, Author, User
from rest_framework import status
import json
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist



@api_view(["GET"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def get_all_users(request):
  users = User.objects.all()
  serializer = UserSerializer(users, many=True)
  return JsonResponse({'users': serializer.data}, safe=False, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_auth(request):
    serialized = UserSerializer(data=request.data)
    if serialized.is_valid():
        serialized.save()
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def get_user(request):
  user = request.query_params["id"]
  data = User.objects.filter(id=user)
  serializer = UserSerializer(data, many=True)
  return JsonResponse({'user': serializer.data}, safe=False, status=status.HTTP_200_OK)

@api_view(["PUT"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def put_user(request, id):
    payload = json.loads(request.body)
    try:
        data = User.objects.filter(id=id)
        data.update(**payload)
        user = User.objects.get(id=id)
        serializer = UserSerializer(user)
        return JsonResponse({'User': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
      return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
      return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["PATCH"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def patch_user(request, id):
    payload = json.loads(request.body)
    try:
        data = User.objects.filter(id=id)
        data.update(**payload)
        user = User.objects.get(id=id)
        serializer = UserSerializer(user)
        return JsonResponse({'user': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
      return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
      return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def delete_user(request, id):
  try:
    user = User.objects.get(pk = 1)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  except ObjectDoesNotExist as e:
    return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
  except Exception:
    return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)