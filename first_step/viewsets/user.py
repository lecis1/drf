from rest_framework import viewsets
from django.contrib.auth.models import User, Group
from first_step.serializers.user import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑API路径
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    允许组查看或编辑API路径
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer