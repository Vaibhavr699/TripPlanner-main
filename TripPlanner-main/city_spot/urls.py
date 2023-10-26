from django.urls import path 
from .views import index, spot_detail, signup, logout, login, search_spot, create_trip, add_spot, user_trip_list, user_trip_detail, user_trip_delete

urlpatterns = [
    path('', index, name="index"),
    path('spot/<str:pk>/', spot_detail, name="spot-detail"),
    path('search-spot/', search_spot, name="search_spot"),
    path('create-trip/', create_trip, name="create-trip"),
    path('add-spot/', add_spot, name="add-spot"),

    path('my-trip-list/', user_trip_list, name="user-trip-list"),
    path('my-trip/<str:pk>/', user_trip_detail, name="user-trip-detail"),
    path('my-trip-delete/<str:pk>/', user_trip_delete, name="user-trip-delete"),

    path('account/signup/', signup, name="signup"),
    path('account/login/', login, name="login"),
    path('account/logout/', logout, name="logout"),
]