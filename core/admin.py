from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from core.models import Usuario, Contatos, Dolar, Indice, Banner,saq

admin.site.register(Usuario)
admin.site.register(Contatos)
admin.site.register(Dolar)
admin.site.register(Indice)
admin.site.register(Banner)
admin.site.register(saq)





class UsuarioAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password",'password_confirmation', 'banner')}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", "foto", "telefone", "banner")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )