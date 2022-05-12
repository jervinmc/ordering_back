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


class Transaction(models.Model):
    product_id=models.CharField(_('tattoo_name'),max_length=255,blank=True,null=True)
    price = models.DecimalField(_('price'),max_digits=20, decimal_places=2,default=0.0)
    user_id=models.CharField(_('user_id'),max_length=255,blank=True,null=True)
    status=models.CharField(_('status'),max_length=255,blank=True,null=True)
    fullname=models.CharField(_('fullname'),max_length=255,blank=True,null=True)
    address=models.CharField(_('address'),max_length=255,blank=True,null=True)
    users_profile=models.CharField(_('users_profile'),max_length=255,blank=True,null=True)
    subtotal=models.CharField(_('subtotal'),max_length=255,blank=True,null=True)
    quantity=models.IntegerField(_('quantity'),blank=True,null=True,default=0)
    image=models.CharField(_('image'),max_length=255,blank=True,null=True)
    size=models.CharField(_('size'),max_length=255,blank=True,null=True)
    color=models.CharField(_('color'),max_length=255,blank=True,null=True)
    class Meta:
        ordering = ["-id"]
