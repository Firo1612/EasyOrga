from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .serializers import EventSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Event
import json

@login_required
def kalender(request):
    return render(request,'kalender.html')


@api_view(['GET', 'POST'])
def event_list_create(request):
    if request.method == 'GET':
        events = Event.objects.filter(user=request.user)
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = request.data
        data['user'] = request.user.id  # Das Event dem aktuell angemeldeten Benutzer zuweisen
        serializer = EventSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def event_update(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'PUT':
        data = json.loads(request.body)
        event.title = data.get('title', event.title)
        event.start = data.get('start', event.start)
        event.end = data.get('end', event.end)
        event.save()
        return JsonResponse({'message': 'Event updated successfully'})
    return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'DELETE':
        event.delete()
        return JsonResponse({'message': 'Event deleted successfully'})
    return JsonResponse({'error': 'Invalid method'}, status=405)