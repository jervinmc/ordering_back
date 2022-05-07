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


class InventoryReport(models.Model):
    product_name=models.CharField(_('tattoo_name'),max_length=255,blank=True,null=True)
    # stocks = models.DecimalField(_('stocks'),max_digits=20, decimal_places=2,default=0.0)
    quantity=models.CharField(_('quantity'),max_length=255,blank=True,null=True)
    stocks=models.IntegerField(_('stocks'),blank=True,null=True,default=0)
    status=models.CharField(_('status'),max_length=255,blank=True,null=True)
    # image = models.ImageField(
    #     _('image'), upload_to=nameFile, default="uploads/Cases.png")
    class Meta:
        ordering = ["-id"]
