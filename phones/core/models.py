from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator# Create your models here.


class Country(models.Model):

    name = models.CharField(_("Country Name"), max_length=30, unique=True) 
    code = models.CharField(_("Country Code"), max_length=3, unique=True)   

    class Meta:
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Country_detail", kwargs={"pk": self.pk})




class Brand(models.Model):

    name = models.CharField(_("Brand Name"), max_length=50, unique=True)
    country = models.ForeignKey("core.Country", verbose_name=_("Nationality"), on_delete=models.DO_NOTHING, related_name="+")
    

    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Brand_detail", kwargs={"pk": self.pk})




class Phone(models.Model):

    name = models.CharField(_("Model"), max_length=64, unique=True)
    brand = models.ForeignKey("core.Brand", to_field="name",  verbose_name=_("Brand"), on_delete=models.DO_NOTHING)
    price = models.PositiveIntegerField(_("Price"))
    color = models.CharField(_("Color"), max_length=50)
    #FIXME What if two color of a Phone??
    size = models.FloatField(_("Display size"), validators=[
        MinValueValidator(0, message='Value must be greater than or equal to 0.'),
    ])
    quantity = models.PositiveIntegerField(_("Quantity"))
    built = models.ForeignKey("core.Country", to_field="name", verbose_name=_("Made IN"), on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = _("Phone")
        verbose_name_plural = _("Mobile Phones")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Phone_detail", kwargs={"pk": self.pk})

    @property
    def nationality(self):
        return self.brand.country.name 
    @property
    def exist(self):
        return self.quantity >= 0