from django.db import models
from django.contrib.auth.models import AbstractUser

class DashboardItem(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title
    
class MyModel(models.Model):
    image = models.ImageField(upload_to='images/')
class CheckNumber(models.Model):
    number_field = models.IntegerField()
    # Add other fields as needed

#Tambahan Rainal
#class CAO1(AbstractUser):
    # Your custom fields and methods here

    #class Meta:
        # Set a unique related_name for groups and user_permissions
        #permissions = [
            #('can_do_something', 'Can do something'),
            # Add other permissions as needed
        #]
    

# Tambahan Tama

class Application(models.Model):
    group_parent = models.IntegerField(blank=True, null=True)
    name_app = models.CharField(max_length=50, blank=True, null=True)
    ip_app = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'applications'

class KodeBankDummy(models.Model):
    sandi_kliring = models.CharField(max_length=255)
    nama_bank = models.CharField(max_length=255)
    BIC = models.CharField(max_length=255)
    kode_wilayah = models.CharField(max_length=255)
    nama_wilayah = models.CharField(max_length=255)
    status = models.BooleanField(default=True)  # True untuk aktif, False untuk nonaktif
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sandi_kliring} - {self.nama_bank}"
    
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, pn, password=None):
        if not pn:
            raise ValueError('PN harus diatur')
        user = self.model(pn=pn)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, pn, password):
        user = self.create_user(pn=pn, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):
    pn = models.CharField(unique=True, max_length=10)  # PN sebagai username
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'pn'

    objects = CustomUserManager()

    def __str__(self):
        return self.pn
# Done Tama

#DB CLEANSING
class CleansingBank (models.Model):
    TRX_TYPE  = models.CharField(max_length=50, null=True)
    MNT_STATUS  = models.CharField(max_length=50, null=True)
    ISPROCESS  = models.CharField(max_length=50, null=True)
    ISGENERATE  = models.CharField(max_length=50, null=True)
    ISCHANGE  = models.CharField(max_length=50, null=True)
    NO = models.DateTimeField(null=True)
    SOR_POTONG = models.DateTimeField(null=True)
    
    
    class Meta:
        db_table = 'INWARDCNNDG'

# DB RETUR
class ReturBankLain (models.Model):
    SOR = models.CharField(max_length=255, null=True)
    TRX_STATUS = models.CharField(max_length=255, null=True)
    STATUS_PROCESS = models.CharField(max_length=255, null=True)
    
    class Meta:
        db_table = 'ICS_RETUR_BANK_LAIN'
        db_table = 'ICS_RETUR_BANK_LAIN_ESB_LOG'
        db_table = 'ICS_RETUR_BANK_LAIN_LOG'
        db_table = 'UPDATE ICS_RETUR_BANK_LAIN SET STATUS_PROCESS'
