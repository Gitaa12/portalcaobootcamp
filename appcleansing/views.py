from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView


# Anggitia
from django.shortcuts import render
from .models import CleansingBank, ReturBankLain


def spbi_page(request):
    return render(request, 'SPBI/main-spbi.html')

#updateanggitia
def update_cleansingbank_page(request):
    returbank_list= ReturBankLain.objects.using('BRIICSS').all()

    # Proses pencarian jika ada query search
    # search_query = request.GET.get('search')
    # if search_query:
    #     returbank_list = returbank_list.filter(nama_bank__icontains=search_query)

    return render(request, 'update_cleansingbank.html', {'returbank_list': returbank_list})


def update_briva_page(request):
    briva_list= CleansingBank.objects.using('BRIICSS').all()

    # Proses pencarian jika ada query search
    # search_query = request.GET.get('search')
    # if search_query:
    #     returbank_list = returbank_list.filter(nama_bank__icontains=search_query)

    return render(request, 'update_briva.html', {'briva_list': briva_list})
