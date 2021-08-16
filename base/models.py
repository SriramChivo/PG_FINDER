from django.db import models
import uuid


class BaseModelClass(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:

        abstract = True
