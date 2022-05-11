from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
# Create your models here.

def nameFile(instance, filename):
    """
    Custom function for naming image before saving.
    """
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)

    return 'uploads/{filename}'.format(filename=filename)


class Taccount(models.Model):
    account=models.CharField(_('account'),max_length=255,blank=True,null=True)
    debit=models.DecimalField(_('debit'),max_digits=20, decimal_places=2,default=0.0)
    credit=models.DecimalField(_('credit'),max_digits=20, decimal_places=2,default=0.0)
    date=models.CharField(_('date'),max_length=255,blank=True,null=True)
    class Meta:
        ordering = ["id"]
