from django.contrib.auth import get_user_model
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse

# Create your models here.

current_user_models = get_user_model()


class UserProfiles(models.Model):

    user_id = models.OneToOneField(current_user_models, on_delete=CASCADE)
    user_Address = models.CharField(verbose_name="Address", max_length=100)
    user_phone_number = models.CharField(
        verbose_name="Phone Number", max_length=10, validators=[MinLengthValidator(10)])

    class Meta:
        verbose_name = "User_Profile"
        verbose_name_plural = "UserProfile"

    def __str__(self):
        return self.user_id.username

    def get_absolute_url(self):
        return reverse("user_detail", kwargs={"pk": self.pk})


class UserFiles(models.Model):

    def get_filename_aadhar(ins, filename):
        return f"{ins.user.username}/aadhar/{filename}"

    def get_filename_pan(ins, filename):
        return f"{ins.user.username}/pancard/{filename}"

    user = models.ForeignKey(
        current_user_models, related_name="user_files", on_delete=CASCADE)
    aadhar = models.FileField(upload_to=get_filename_aadhar)
    pan = models.FileField(upload_to=get_filename_pan)

    def __str__(self):
        return f"{self.user} - Files"

    class Meta:

        verbose_name_plural = "UserFiles"
