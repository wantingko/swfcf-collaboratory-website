from django.contrib.auth import login
from django.shortcuts import render
from django.urls import reverse
from collaboratory_api.forms import CustomUserCreationForm

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .serializers import *
from .models import *
# from .models import Region, Role, Cause, User, Organization, Event, Channel, Announcement, Post, Organization_Region, Organization_Cause_Alignment, User_Event_Attendance

class RegionViewSet(viewsets.ModelViewSet):
    serializer_class = RegionSerializer
    queryset = Region.objects.all().order_by('region_id')

class RoleViewSet(viewsets.ModelViewSet):
    serializer_class = RoleSerializer
    queryset = Role.objects.all().order_by('role_id')

class CauseViewSet(viewsets.ModelViewSet):
    serializer_class = CauseSerializer
    queryset = Cause.objects.all().order_by('cause_id')

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by('user_id')

class OrganizationViewSet(viewsets.ModelViewSet):
    serializer_class = OrganizationSerializer
    queryset=Organization.objects.all().order_by('name')

class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all().order_by('event_id')

class ChannelViewSet(viewsets.ModelViewSet):
    serializer_class = ChannelSerializer
    queryset = Channel.objects.all().order_by('channel_id')

class AnnouncementViewSet(viewsets.ModelViewSet):
    serializer_class = AnnouncementSerializer
    queryset = Announcement.objects.all().order_by('announcement_id')

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all().order_by('post_id')

class OrganizationRegionViewSet(viewsets.ModelViewSet):
    serializer_class = OrganizationRegionSerializer
    queryset = Organization_Region.objects.all().order_by('id')

class OrganizationCauseViewSet(viewsets.ModelViewSet):
    serializer_class = OrganizationCauseSerializer
    queryset = Organization_Cause_Alignment.objects.all().order_by('id')

class UserEventViewSet(viewsets.ModelViewSet):
    serializer_class = UserEventSerializer
    queryset = User_Event_Attendance.objects.all().order_by('id')

## Organization API Views ##
@api_view(['GET', 'POST'])
def organizations_list(request):
    if request.method == 'GET':
        data = Organization.objects.all()
        serializer = OrganizationSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = OrganizationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def organizations_detail(request, pk):
    try:
        organization = Organization.objects.get(pk=pk)
    except Organization.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = OrganizationSerializer(organization, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        organization.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

## User API Views ##
@api_view(['GET', 'POST'])
def users_list(request):
    if request.method == 'GET':
        data = User.objects.all()
        serializer = UserSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def users_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# dashboard render
def dashboard(request):
    return render(request, "collaboratory_api/dashboard.html")

#user registration
def register(request):
    if request.method == "GET":
        return render(
            request, "collaboratory_api/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))