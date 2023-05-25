from rest_framework import generics
from .models import Event
from .serializers import EventSerializer

class EventListView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


# # Create event
# class EventCreateView(generics.CreateAPIView):
#     queryset = Event.objects.all()
#     serializer_class = EventSerializer

# # Retrieve event by ID
# class EventDetailView(generics.RetrieveAPIView):
#     queryset = Event.objects.all()
#     serializer_class = EventSerializer
#     lookup_field = 'id'

# # Update event
# class EventUpdateView(generics.UpdateAPIView):
#     queryset = Event.objects.all()
#     serializer_class = EventSerializer
#     lookup_field = 'id'

# # Delete event
# class EventDeleteView(generics.DestroyAPIView):
#     queryset = Event.objects.all()
#     serializer_class = EventSerializer
#     lookup_field = 'id'

# # List events
# class EventListView(generics.ListAPIView):
#     queryset = Event.objects.all()
#     serializer_class = EventSerializer
