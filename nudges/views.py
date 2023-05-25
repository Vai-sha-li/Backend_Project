from rest_framework import generics
from .models import Nudge
from .serializers import NudgeSerializer

class NudgeListView(generics.ListCreateAPIView):
    queryset = Nudge.objects.all()
    serializer_class = NudgeSerializer

class NudgeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Nudge.objects.all()
    serializer_class = NudgeSerializer
