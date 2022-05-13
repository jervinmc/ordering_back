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


class Carts(models.Model):
    user_id=models.CharField(_('user_id'),max_length=255,blank=True,null=True)
    quantity=models.IntegerField(_('quantity'),blank=True,null=True,default=0)
    price = models.DecimalField(_('price'),max_digits=20, decimal_places=2,default=0.0)
    product_name=models.CharField(_('product_name'),max_length=255,blank=True,null=True)
    product_id=models.CharField(_('product_id'),max_length=255,blank=True,null=True)
    image=models.CharField(_('image'),max_length=255,blank=True,null=True)
    size=models.CharField(_('size'),max_length=255,blank=True,null=True)
    color=models.CharField(_('color'),max_length=255,blank=True,null=True)
    # image = models.ImageField(
    #     _('image'), upload_to=nameFile, default="uploads/Cases.png")
    class Meta:
        ordering = ["-id"]
