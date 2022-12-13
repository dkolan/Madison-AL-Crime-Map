from django.urls import path
from apis import views

urlpatterns = [
    path('incidents', views.IncidentList.as_view(), name='incident_list'),
    path('incidents/<int:pk>', views.IncidentDetail.as_view(), name='incident')
]