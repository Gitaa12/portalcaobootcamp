from django.db import models
from django.contrib.auth.models import AbstractUser

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
