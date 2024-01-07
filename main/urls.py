from django.contrib import admin
from django.urls import path, include
from views import views, about, absences, activities, assignments, calendar, coaches, contact, gallery, messages, \
    offer, payments, settings, upcoming_classes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('login', views.login_user, name='login-user'),

    path('about/', about.get_about, name='about-get'),
    path('about/update', about.update_about, name='about-update'),  # only Rick

    path('', activities.get_activities, name='activities-get'),
    path('activity/add', activities.add_activity, name='activity-add'),  # only coaches
    path('activity/update/<int:activity_id>', activities.update_activity, name='activity-update'),  # only coaches
    path('activity/delete/<int:activity_id>', activities.delete_activity, name='activity-delete'),  # only coaches
    path('events/', activities.get_activities, name='events-get'),
    path('event/add', activities.add_activity, name='event-add'),  # only coaches
    path('event/update/<int:activity_id>', activities.update_activity, name='event-update'),  # only coaches
    path('event/delete/<int:activity_id>', activities.delete_activity, name='event-delete'),  # only coaches

    path('coaches/', coaches.get_coaches, name='coaches-get'),
    path('coach/add', coaches.add_coach, name='coach-add'),  # only Rick
    path('coach/update/<int:coach_id>', coaches.update_coach, name='coach-update'),
    path('coach/delete/<int:coach_id>', coaches.delete_coach, name='coach-delete'),  # only Rick

    path('contact/', contact.get_contact, name='contact-get'),
    path('contact/update', contact.update_contact, name='contact-update'),  # only Rick

    path('gallery/', gallery.get_gallery, name='gallery-get'),
    path('gallery/update', gallery.add_image, name='gallery-add'),  # only coaches
    path('gallery/delete/<int:image_id>', gallery.delete_image, name='gallery-delete'),  # only coaches

    path('offer/', offer.get_offer, name='offer-get'),
    path('offer/add', offer.add_offer, name='offer-add'),
    path('offer/update/<int:offer_id>', offer.update_offer, name='offer-update'),
    path('offer/delete/<int:offer_id>', offer.delete_offer, name='offer-delete'),
    path('offer/sign_in', offer.sign_in, name='offer-sign-in'),  # only not logged in and students

    path('user/', upcoming_classes.get_upcoming_classes, name='upcoming-classes-get'),

    path('user/absences', absences.get_absences, name='absences-get'),  # only coaches
    path('user/absence/request', absences.request_absence, name='absence-request'),  # only coaches
    # path('user/absence/request/<id>/cancel', views.absence_cancel_request, name='absence-cancel-request'),  # only coaches

    path('user/assignments/', assignments.get_assignments, name='assignments-get'),
    path('user/assignments/<int:class_id>', assignments.get_assignments, name='assignments-get'),
    path('user/assignments/<int:class_id>/<int:user_id>', assignments.get_assignments, name='assignments-get'),
    path('user/assignment/request/<int:class_id>', assignments.request_assignment, name='assignment-request'),  # only students
    path('user/assignment/update/<int:assignment_id>', assignments.update_assignment, name='assignment-update'),  # only students
    # path('user/assignment/request/<id>/delete', views.assignment_request_delete, name='assignment-request-delete'),  # only students

    path('user/calendar/', calendar.get_calendar, name='calendar-get'),
    path('user/calendar/events', calendar.get_calendar_events, name='calendar-get-events'),
    # path('user/calendar/(class)/reschedule', views.calendar_reschedule, name='calendar-reschedule'),  # only coaches

    path('user/messages/', messages.get_messages, name='messages-get'),

    path('user/payments/', payments.get_payments, name='payments-get'),
    path('user/payments/pay', payments.pay_for_classes, name='payments-pay'),

    path('user/settings/', settings.get_settings, name='settings-get'),
    path('user/settings/password/update', settings.update_password, name='settings-password-update'),
    path('user/settings/font/update', settings.update_font, name='settings-font-update'),
    path('user/settings/chat-notifications/update', settings.update_chat_notifications,
         name='settings-chat-notifications-update')
]
