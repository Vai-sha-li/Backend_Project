from django.urls import path
from .views import NudgeListView, NudgeDetailView

app_name = 'nudges'

urlpatterns = [
    path('nudges/', NudgeListView.as_view(), name='nudge-list'),
    path('nudges/<int:pk>/', NudgeDetailView.as_view(), name='nudge-detail'),
]
