from enum import unique

from base.models import BaseModelClass

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.expressions import F
from django.db.models.fields import related
from django.core.exceptions import ValidationError

from .choices import PgChoices, PgLocationChoices

User = get_user_model()


class PayingGuest(BaseModelClass):

    def default_address():  # noqa
        return "X street , Y lane, Z city , pincode - 000000 "

    def validate_phone_numbers(value):
        if not len(value):
            raise ValidationError("Phone number should be 10 digits")

    name = models.CharField(
        verbose_name="Name of the pg", unique=True, max_length=100
    )
    category = models.CharField(choices=PgChoices.choices, max_length=6)
    city = models.CharField(choices=PgLocationChoices.cities, max_length=19)
    address = models.CharField(
        verbose_name="Exact Address of PG", max_length=250, default=default_address)
    amenities = models.ManyToManyField("Amenities", related_name="amenities")  # noqa
    daily_rent_charges_range = models.CharField(
        max_length=100, blank=False, null=False, default="Rs 250 - Rs 450")
    monthly_rental_charge = models.CharField(
        max_length=100, blank=False, null=False, default="Rs 5000 - Rs 6000")
    no_of_rooms_present = models.IntegerField(default=0)
    no_of_beds_present = models.IntegerField(default=0)
    pg_phone_no = models.CharField(
        validators=[validate_phone_numbers], max_length=10, unique=True)

    def __str__(self) -> str:
        return self.name


class Amenities(BaseModelClass):

    name = name = models.CharField(
        verbose_name="Name of the Amenities you can provide", unique=True, max_length=100
    )

    def __str__(self) -> str:
        return self.name


class PgImage(BaseModelClass):

    def get_upload_filename(instance, filename):
        return f"{instance.pg.name}/{filename}"

    pg = models.ForeignKey(
        "PayingGuest", related_name="pgimages", on_delete=CASCADE)
    image = models.ImageField(upload_to=get_upload_filename)

    class Meta:

        verbose_name_plural = "PgImages"

    def __str__(self):
        return f"{self.pg.name} -  Image"


class PgRoom(BaseModelClass):

    pg = models.ForeignKey(
        "PayingGuest", verbose_name=("Which PG this room belongs to"), on_delete=models.CASCADE)
    room_number = models.IntegerField(unique=True)

    class Meta:
        verbose_name_plural = "PgRooms"
        unique_together = ("pg", "room_number")

    def __str__(self):
        return f"{self.pg.name} - Room Number: {self.room_number}"


class PgCot(BaseModelClass):

    pg = models.ForeignKey(
        "PayingGuest", verbose_name=("Which PG this cot belongs to"), on_delete=models.CASCADE)
    pg_room = models.ForeignKey("PgRoom", verbose_name=(
        "Which PG this cot belongs to"), on_delete=models.CASCADE)
    cot_number = models.IntegerField()
    occupied_by = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="get_occupied_user", null=True)
    daily_rent = models.IntegerField(default=250)
    monthly_rent = models.IntegerField(default=5500)
    is_rent_paid = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "PgCots"
        unique_together = ("pg", "cot_number", "pg_room")

    def __str__(self):
        return f"{self.pg.name} - Room Number: {self.pg_room.room_number} - Cot Number {self.cot_number}"


class Comment(models.Model):

    pg = models.ForeignKey(
        "PayingGuest", on_delete=models.CASCADE, null=True, blank=True, related_name="pg_comments")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="get_comments")
    detail = models.CharField(max_length=1500)
    date = models.DateTimeField(auto_now_add=True)
    pgroom = models.ForeignKey(
        "PgRoom", on_delete=models.CASCADE, null=True, blank=True, related_name="pg_room_comments")

    def __str__(self):
        return self.detail
