from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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


class TaskDetail(APIView):
    """
    Update or Delete a task instance
    """
    def get_object(self, pk):
        return get_object_or_404(Task, pk=pk)

    def delete(self, request, pk, format=None):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
