from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.
from .models import DashboardItem, CheckNumber


from .forms import formsCheckNumber

# Tama
from django.shortcuts import render, redirect,  get_object_or_404
from .forms import ApplicationForm
from .models import Application, KodeBankDummy, CleansingBank, ReturBankLain


def dashboard(request):
    items = DashboardItem.objects.all()
    return render(request, 'dashboard.html', {'items': items})

def sandbox_page(request):
    return render(request, 'sandbox.html')

# def changekodebank_page(request):
#    return render(request, 'changekodebank.html')

def spbi_page(request):
    return render(request, 'SPBI/main-spbi.html')

def querybox_page(request):
    return render(request, 'querybox.html')

def login(request):
    return render(request, 'login.html')

def CheckNmbr(request):
    if request.method == 'POST':
        form = formsCheckNumber(request.POST)
        if form.is_valid():
            # Get the number from the form
            number_value = form.cleaned_data['number_field']

            # Perform a SELECT query based on the number
            query_result = CheckNumber.objects.filter(number_field=number_value)

            # Pass the query result to the template
            return render(request, 'CheckNumber.html', {'query_result': query_result, 'form': form})

    else:
        form = formsCheckNumber()

    return render(request, 'CheckNumber.html', {'form': form})


# Tambahan Tama
def show_applications(request):
    applications = Application.objects.all()

    if 'search' in request.GET:
        search_query = request.GET['search']
        applications = applications.filter(name_app__icontains=search_query)

    return render(request, 'applications.html', {'applications': applications})


def create_application(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_applications')  # Redirect ke halaman tampilan aplikasi setelah data dibuat
    else:
        form = ApplicationForm()
    return render(request, 'create_application.html', {'form': form})

def update_application(request, app_id):
    application = get_object_or_404(Application, id=app_id)
    if request.method == 'POST':
        form = ApplicationForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            return redirect('show_applications')  # Redirect ke halaman tampilan aplikasi setelah data diperbarui
    else:
        form = ApplicationForm(instance=application)
    return render(request, 'update_application.html', {'form': form})


def changekodebank_page(request):
    kodebank_list = KodeBankDummy.objects.all()

    # Proses pencarian jika ada query search
    search_query = request.GET.get('search')
    if search_query:
        kodebank_list = kodebank_list.filter(nama_bank__icontains=search_query)

    return render(request, 'changekodebank.html', {'kodebank_list': kodebank_list})

from .models import KodeBankDummy
from django.http import JsonResponse
from .forms import KodeBankForm

def update_kodebank(request, pk):
    kodebank = get_object_or_404(KodeBankDummy, pk=pk)
    form = KodeBankForm(request.POST or None, instance=kodebank)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'error': form.errors}, status=400)
    return render(request, 'update_kodebank.html', {'form': form})

from .models import CleansingBank
from django.http import JsonResponse
from .forms import CleansingBankForm
#updateanggitia
def update_cleansingbank(request, pk):
    kodebank = get_object_or_404(CleansingBank, pk=pk)
    form = CleansingBankForm(request.POST or None, instance=kodebank)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'error': form.errors}, status=400)
    return render(request, 'update_cleansingbank.html', {'form': form})

from .models import ReturBankLain
from django.http import JsonResponse
from .forms import ReturBankLainForm

def update_returbank(request, pk):
    kodebank = get_object_or_404(ReturBankLain, pk=pk)
    form = ReturBankLainForm(request.POST or None, instance=kodebank)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'error': form.errors}, status=400)
    return render(request, 'update_returbank.html', {'form': form})
