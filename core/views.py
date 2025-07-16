from rest_framework.response import Response
from rest_framework import generics, authentication, mixins, permissions
from .models import Task
from .serializers import TaskSerializer
from django.shortcuts import get_object_or_404
from .authentication import TokenAuthentication
from .permissions import IsStaffEditorPermission
from rest_framework.decorators import api_view
from rest_framework.response import Response


class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)
        # send a django signal


task_list_create_view = TaskListCreateView.as_view()


class TaskDetailAPIView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # lookup_field = 'pk ??


task_detail_view = TaskDetailAPIView.as_view()


class TaskUpdateAPIView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


task_update_view = TaskUpdateAPIView.as_view()


class TaskDestroyAPIView(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


task_destroy_view = TaskDestroyAPIView.as_view()



#
# @api_view(['GET', 'POST'])
# def task_alt_view(request, pk=None, *args, **kwargs):
#     method = request.method
#
#     if method == "GET":
#         if pk is not None:
#             # detail view
#             obj = get_object_or_404(Task, pk=pk)
#             data = TaskSerializer(obj, many=False).data
#             return Response(data)
#         # list view
#         queryset = Task.objects.all()
#         data = TaskSerializer(queryset, many=True).data
#         return Response(data)
#
#     if method == "POST":
#         # create an item
#         serializer = TaskSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             title = serializer.validated_data.get('title')
#             content = serializer.validated_data.get('content') or None
#             if content is None:
#                 content = title
#             serializer.save(content=content)
#             return Response(serializer.data)
#         return Response({"invalid": "not good data"}, status=400)