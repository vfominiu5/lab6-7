from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^logout$', views.logout_view, name='logout'),
    url(r'^success_authorization_dumb$', views.success_authorization_dumb, name='success_authorization_dumb'),
    url(r'^success_authorization$', views.success_authorization, name='success_authorization'),
    url(r'^authorization/$', views.authorization, name='authorization'),
    url(r'^registration_dumb/$', views.registration_dumb, name='registration_dumb'),
    url(r'^registration_traveler/$',views.registration_traveler, name='registration_traveler'),
    url(r'^news/(?P<id>(\d+))$',views.single_news, name='news'),
    url(r'^travelers/$',views.TravelerList.as_view(),name='traveler_list'),
    url(r'^hotels/$',views.HotelList.as_view(),name='hotel_list'),
    url(r'^bookings/$',views.BookingList.as_view(),name='booking_list'),
    url(r'^$',views.index,name='index')
]
