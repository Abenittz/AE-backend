from django.urls import path, include
from rest_framework.routers import DefaultRouter


# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


from . import views

router = DefaultRouter()
router.register(r'api/attendees', views.AttendeeViewSet)
router.register(r'api/events', views.EventViewSet)
router.register(r'api/speakers', views.SpeakerViewSet)
router.register(r'api/sponsors', views.SponsorViewSet)
router.register(r'api/users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
    path('api/token/', views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('api/event/register/', views.EventRegistrationView.as_view(), 
         name='event-registration'),
    
    path('api/attendee/register/', views.AttendeeRegistrationView.as_view(),
         name='attendee-registration'),
    
    path('api/speaker/register/', views.SpeakerRegistrationView.as_view(),
         name='speaker-registration'),

    path('api/sponsor/register/', views.SponsorRegistrationView.as_view(),
         name='sponsor-registration'),

    path('api/schedule/register/', views.ScheduleRegistrationView.as_view(),
         name='schedule-registration'),

    path('api/users/<int:pk>/',
         views.UserViewSet.as_view({'get': 'retrieve'}), name='user-detail'),


    path('api/download-attendees-pdf/<int:event_id>/',
         views.AttendeesPDFDownload.as_view(), name='download-attendees-pdf'),
    
    path('api/download-event-report-pdf/<int:event_id>/',
         
         views.EventReportPDFDownload.as_view(), name='download-event-report-pdf'),
    path('api/download-event-schedule-pdf/<int:event_id>/',
         
         views.SchedulePDFDownload.as_view(), name='download-event-schedule-pdf'),
]
