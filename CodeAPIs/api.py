from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from CodeAPIs.serializers import UserSerializer
from CodeAPIs.models import User


class UserList(APIView):

    def get(self, request):
        model = User.objects.all()
        serializer = UserSerializer(model, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Added Successfully", status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetails(APIView):

    def get(self, request, employee_id):
        try:
            model = User.objects.get(eid=employee_id)
        except User.DoesNotExist:
            return Response("User Not Found", status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(model)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, employee_id):
        try:
            model = User.objects.get(eid=employee_id)
        except User.DoesNotExist:
            return Response("User Not Found", status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("User Successfully Updated", status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, employee_id):
        try:
            model = User.objects.get(eid=employee_id)
        except User.DoesNotExist:
            return Response("User Not Found", status=status.HTTP_404_NOT_FOUND)

        model.delete()
        return Response("User Deleted Successfully", status=status.HTTP_200_OK)
