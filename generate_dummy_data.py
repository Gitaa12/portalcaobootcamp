import os
import django

# Atur environment variable DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portal_cao.settings')

# Lakukan konfigurasi Django
django.setup()

# Sekarang Anda dapat mengimpor model Django atau modul lain yang membutuhkan pengaturan Django
from dashboard.models import KodeBankDummy
from django.utils import timezone
from faker import Faker

fake = Faker()

def generate_dummy_data(num_records):
    for _ in range(num_records):
        kodebank = KodeBankDummy(
            sandi_kliring=fake.word(),
            nama_bank=fake.company(),
            BIC=fake.word(),
            kode_wilayah=fake.city(),
            nama_wilayah=fake.country(),
            status=fake.boolean(),
            timestamp=timezone.now()
        )
        kodebank.save()

if __name__ == "__main__":
    num_records = 10  # Jumlah data dummy yang ingin Anda buat
    generate_dummy_data(num_records)
