from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe
from phonenumber_field.widgets import PhoneNumberPrefixWidget

from .models import (
    Establishment,
    Kitchen,
    Service,
    Event,
    Review,
    Type,
    ZoneEstablishment,
    ImageEstablishment,
    WorkEstablishment,
    SocialEstablishment,
)


class ContactForm(forms.ModelForm):
    class Meta:
        widgets = {
            "telephone": PhoneNumberPrefixWidget(initial="RU"),
        }


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id",)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("id",)
    empty_value_display = "-пусто-"


@admin.register(Kitchen)
class KitchenAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "slug")
    empty_value_display = "-пусто-"


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "slug")
    empty_value_display = "-пусто-"


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "slug")
    empty_value_display = "-пусто-"


class ZonesInLine(admin.TabularInline):
    model = ZoneEstablishment


class SocialInLine(admin.TabularInline):
    model = SocialEstablishment


class ImageInLine(admin.TabularInline):
    model = ImageEstablishment


class WorkInLine(admin.TabularInline):
    model = WorkEstablishment


@admin.register(Establishment)
class EstablishmentAdmin(admin.ModelAdmin):
    form = ContactForm
    list_display = (
        "name",
        "id",
        "preview",
        "email",
        "is_verified",
    )
    list_filter = ("name",)
    empty_value_display = "-пусто-"
    inlines = (ZonesInLine, WorkInLine, ImageInLine, SocialInLine)

    def preview(self, obj):
        return mark_safe(
            f'<img src="{obj.poster.url}" style="max-height: 50px;">'
        )

    preview.short_description = "Превью"
