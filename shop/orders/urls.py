from django.urls import path, include

urlpatterns = [
    path('api/', include('orders.api.v1.urls')),
]