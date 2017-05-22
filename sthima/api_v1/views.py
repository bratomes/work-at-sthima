from rest_framework.views import APIView
from rest_framework.response import Response

from todo.models import Task

from .serializers import TaskSerializer


class TaskList(APIView):
    """
    List all tasks or create a new one
    """
    def get(self, request, format=None):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
