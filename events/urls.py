from django.urls import path
from .views import EventListView, EventDetailView
from django.conf import settings
from django.conf.urls.static import static
app_name = 'events'

urlpatterns = [
    path('events/', EventListView.as_view(), name='event-list'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
