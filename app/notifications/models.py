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


class Notification(models.Model):
    user_id=models.CharField(_('user_id'),max_length=255,blank=True,null=True)
    viewed=models.CharField(_('stocks'),max_length=255,blank=True,null=True)
    descriptions=models.CharField(_('descriptions'),max_length=255,blank=True,null=True)
    module=models.CharField(_('module'),max_length=255,blank=True,null=True)
    image=models.CharField(_('image'),max_length=255,blank=True,null=True)
    users_profile=models.CharField(_('users_profile'),max_length=255,blank=True,null=True)
    class Meta:
        ordering = ["-id"]
