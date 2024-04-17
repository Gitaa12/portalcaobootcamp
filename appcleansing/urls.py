# dashboard/urls.py

from django.urls import path
from .views import spbi_page, update_cleansingbank_page, update_briva_page
from .views import dashboard
from django.contrib.auth.views import LoginView, LogoutView

app_name = "appcleansing"

urlpatterns = [
    path('spbi/', spbi_page, name='spbi'),
    path('returbank/', update_cleansingbank_page, name='update_cleansingbank_page'),
    path('briva/', update_briva_page, name='update_briva_page'),
]