# dashboard/urls.py

from django.urls import path
from .views import dashboard, sandbox_page, changekodebank_page, spbi_page, querybox_page, show_applications,create_application, update_application, update_cleansingbank_page, update_briva_page
from .views import update_kodebank
from .views import dashboard, login, CheckNmbr
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('sandbox/', sandbox_page, name='sandbox'),
    # path('changekodebank/', changekodebank_page, name='changekodebank'),
    path('spbi/', spbi_page, name='spbi'),
    path('querybox/', querybox_page, name='querybox'),
    path('applications/', show_applications, name='show_applications'),
    path('applications/create/', create_application, name='create_application'),
    path('applications/<int:app_id>/update/', update_application, name='update_application'),
    path('changekodebank/', changekodebank_page, name='changekodebank_page'),
    path('update-kodebank/<int:pk>/', update_kodebank, name='update_kodebank'),
    path('returbank/', update_cleansingbank_page, name='update_cleansingbank_page'),
    path('briva/', update_briva_page, name='update_briva_page'),
    path('', dashboard, name='dashboard'),
    
    # path('login/', LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),
    # path('', LogoutView.as_view(), name='logout'),
    path('CheckNumber/', CheckNmbr, name='CheckNmbr'),
]