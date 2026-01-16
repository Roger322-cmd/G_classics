from django.contrib import admin
from django import forms
from .models import SiteSettings, StaticPage

class SiteSettingsForm(forms.ModelForm):
    class Meta:
        model = SiteSettings
        fields = "__all__"
        widgets = {
            "primary_color": forms.TextInput(attrs={"type": "color"}),
            "secondary_color": forms.TextInput(attrs={"type": "color"}),
            "glass_background": forms.TextInput(attrs={"placeholder": "rgba(255,255,255,0.08)"}),
            "glass_border_color": forms.TextInput(attrs={"placeholder": "rgba(255,255,255,0.25)"}),
        }


class SiteSettingsAdmin(admin.ModelAdmin):
    form = SiteSettingsForm

    class Media:
        css = {"all": ("admin/theme_preview.css",)}
        js = ("admin/theme_preview.js",)


admin.site.register(SiteSettings, SiteSettingsAdmin)


@admin.register(StaticPage)
class StaticPageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "slug", "updated_at")
