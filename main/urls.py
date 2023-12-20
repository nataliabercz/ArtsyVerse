from django.contrib import admin
from django.urls import path, include
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('', views.get_activities, name='get-activities'),
    path('activities/add/', views.add_activity, name='add-activity'),
    path('activities/update/', views.update_activity, name='update-activity'),
    # path('activities/delete/', views.delete_activity, name='delete-activity'),
    path('about/', views.get_info, name='get-about'),
    path('coaches/', views.get_coaches, name='get-coaches'),
    # path('coaches/update', views.update_coach, name='update-coach'),
    path('contact/', views.get_contact, name='get-contact'),
    path('events/', views.get_activities, name='get-activities'),
    path('gallery/', views.get_gallery, name='get-gallery'),
    path('gallery/update/', views.update_gallery, name='update-gallery'),
    path('offer/', views.get_offer, name='get-offer'),
    path('user/', views.get_next_classes, name='get-next-classes'),
    path('user/absence/', views.absence, name='absence'),
    # path('user/absence/request', views.request_absence, name='request_absence'),
    path('user/assignments/', views.get_assignments, name='get-assignments'),
    path('user/assignments/request/', views.request_assignments, name='request-assignments'),
    path('user/calendar/', views.get_calendar, name='get-calendar'),
    path('user/calendar/events', views.get_calendar_events, name='get-calendar-events'),
    # path('user/calendar(class)/reschedule', views.get_calendar, name='get-calendar'),
    path('user/chat/', views.chat, name='chat'),
    path('user/feedback/', views.send_feedback, name='send-feedback'),
    path('user/payments/', views.get_payments, name='get-payments'),
    path('user/settings/', views.change_settings, name='change-settings')
]
