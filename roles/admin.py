from django.contrib import admin

from roles.models import BodyRole, InstituteRole

admin.site.register(BodyRole)
admin.site.register(InstituteRole)
