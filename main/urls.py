from django.contrib import admin as adm
from django.urls import path, include
from views import views, about, absences, activities, admin, assignments, calendar, coaches, contact, gallery, \
    messages, offer, payments, settings, upcoming_classes

handler404 = views.error_404
handler500 = views.error_500

urlpatterns = [
    path('admin/', adm.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('login', views.login_user, name='login'),

    path('about/', about.get_about, name='about-get'),
    path('about/update', about.update_about, name='about-update'),
    path('about/upload', about.upload_info_image, name='info-image-upload'),
    path('about/delete/<int:image_id>', about.delete_info_image, name='info-image-delete'),

    path('', activities.get_activities, name='activities-get'),
    path('activity/add', activities.add_activity, name='activity-add'),
    path('activity/update/<int:activity_id>', activities.update_activity, name='activity-update'),
    path('activity/delete/<int:activity_id>', activities.delete_activity, name='activity-delete'),
    path('events/', activities.get_activities, name='events-get'),
    path('event/add', activities.add_activity, name='event-add'),
    path('event/update/<int:activity_id>', activities.update_activity, name='event-update'),
    path('event/delete/<int:activity_id>', activities.delete_activity, name='event-delete'),
    # path('event/ticket/buy/<int:activity_id>', activities.buy_ticket, name='event-ticket-buy'),  # only coaches

    path('coaches/', coaches.get_coaches, name='coaches-get'),
    path('coach/update/<int:coach_id>', coaches.update_coach, name='coach-update'),
    path('coach/delete/<int:coach_id>', coaches.delete_coach, name='coach-delete'),

    path('contact/', contact.get_contact, name='contact-get'),
    path('contact/update', contact.update_contact, name='contact-update'),

    path('gallery/', gallery.get_gallery, name='gallery-get'),
    path('gallery/update', gallery.add_image, name='gallery-add'),
    path('gallery/delete/<int:image_id>', gallery.delete_image, name='gallery-delete'),

    path('offer/', offer.get_offer, name='offer-get'),
    path('offer/add', offer.add_offer, name='offer-add'),
    path('offer/update/<int:offer_id>', offer.update_offer, name='offer-update'),
    path('offer/delete/<int:offer_id>', offer.delete_offer, name='offer-delete'),
    path('offer/sign_in', offer.sign_in, name='offer-sign-in'),  # only not logged in and students

    path('user/', upcoming_classes.get_upcoming_classes, name='upcoming-classes-get'),

    path('user/absences', absences.get_absences, name='absences-get'),  # only coaches
    path('user/absence/request', absences.request_absence, name='absence-request'),  # only coaches
    # path('user/absence/request/<id>/cancel', views.absence_cancel_request, name='absence-cancel-request'),  # only coaches

    path('user/admin/users', admin.get_users, name='users-get'),
    path('user/admin/user/add/<int:group_id>', admin.add_user, name='user-add'),
    path('user/admin/user/update/<int:group_id>/<int:profile_id>', admin.update_user, name='user-update'),
    path('user/admin/user/delete/<int:group_id>/<int:profile_id>', admin.delete_user, name='user-delete'),
    path('user/admin/classes', admin.get_classes, name='classes-get'),
    path('user/admin/class/add', admin.add_class, name='class-add'),
    path('user/admin/class/update/<int:class_id>', admin.update_class, name='class-update'),
    path('user/admin/classes/delete/<int:class_id>', admin.delete_class, name='class-delete'),

    path('user/assignments/', assignments.get_assignments, name='assignments-get'),
    path('user/assignments/<int:class_id>', assignments.get_assignments, name='assignments-get'),
    path('user/assignments/<int:class_id>/<int:user_id>', assignments.get_assignments, name='assignments-get'),
    path('user/assignment/request/<int:class_id>', assignments.request_assignment, name='assignment-request'),
    path('user/assignment/update/<int:assignment_id>', assignments.update_assignment, name='assignment-update'),

    path('user/calendar/', calendar.get_calendar, name='calendar-get'),
    path('user/calendar/events', calendar.get_calendar_events, name='calendar-get-events'),
    # path('user/calendar/reschedule/<int:class_id>', calendar.reschedule_class, name='class-reschedule'),

    path('user/messages/', messages.get_messages, name='messages-get'),
    path('user/messages/<int:recipient_id>', messages.get_messages, name='messages-get'),
    path('user/messages/search', messages.search_recipients, name='messages-recipients-search'),
    path('user/messages/autocomplete/', messages.UserAutocomplete.as_view(), name='user-autocomplete'),
    path('user/message/send', messages.send_message, name='messages-send'),

    path('user/payments/', payments.get_payments, name='payments-get'),
    path('user/payments/pay', payments.pay_for_classes, name='payments-pay'),

    path('user/settings/', settings.get_settings, name='settings-get'),
    path('user/settings/password/reset', settings.reset_password, name='settings-password-reset'),
    path('user/settings/password/update', settings.update_password, name='settings-password-update'),
    path('user/settings/font/update', settings.update_font, name='settings-font-update'),
    path('user/settings/chat-notifications/update', settings.update_chat_notifications,
         name='settings-chat-notifications-update')
]
