from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .models import Task, TaskMember
from django.contrib.auth.models import User
from .serializers import TaskSerializer, TaskMemberSerializer

class TaskViewSet(viewsets.GenericViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    # Fetching list of all tasks
    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    # creating tasks
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success_message':'Task Created Successfully.', 'data': serializer.data}, status=status.HTTP_201_CREATED)

    # fetching sepecific task
    def retrieve(self, request, pk=None):
        task = self.get_object()
        serializer = self.get_serializer(task)
        return Response(serializer.data)

    # updating a task
    def update(self, request, pk=None):
        task = self.get_object()
        serializer = self.get_serializer(task, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    # deleting a task
    def destroy(self, request, pk=None):
        task = self.get_object()
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # adding member to a task
    @action(detail=True, methods=['post'])
    def add_member(self, request, pk=None):
        task = self.get_object()
        user_id = request.data.get('user_id')
        if user_id is None:
            return Response({"detail": "User ID is required."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)
        
         # Check if the user is already a member of the task
        if task.members.filter(user=user).exists():
            return Response({"detail": f"User {user.first_name} {user.last_name} is already a member of task {task.id}."}, status=status.HTTP_400_BAD_REQUEST)
        
        # If user is not already a member, create TaskMember object
        TaskMember.objects.create(task=task, user=user)
        return Response({"detail": f"User {user.first_name} {user.last_name} added to task {task.id}."}, status=status.HTTP_200_OK)

    # removing member from a task
    @action(detail=True, methods=['post'])
    def remove_member(self, request, pk=None):
        task = self.get_object()
        user_id = request.data.get('user_id')
        if user_id is None:
            return Response({"detail": "User ID is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            task_member = TaskMember.objects.get(task=task, user_id=user_id)
            name = task_member.user.first_name
            task_member.delete()
        except TaskMember.DoesNotExist:
            return Response({"detail": "Task member not found."}, status=status.HTTP_404_NOT_FOUND)
        
        return Response({"detail": f"User {name} removed from task {task.id}."}, status=status.HTTP_200_OK)

    # fetching all members of a given task
    @action(detail=True, methods=['get'])
    def members(self, request, pk=None):
        task = self.get_object()
        members = task.members.all()
        serializer = TaskMemberSerializer(members, many=True)
        return Response(serializer.data)

    # updating task status
    @action(detail=True, methods=['put'])
    def update_status(self, request, pk=None):
        task = self.get_object()
        new_status = request.data.get('status')
        if new_status not in dict(Task.status_choices).keys():
            return Response({"detail": "Invalid status value."}, status=status.HTTP_400_BAD_REQUEST)
        
        task.status = new_status
        task.save()
        return Response({"detail": f"Task {task.id} status updated to {new_status}."}, status=status.HTTP_200_OK)
