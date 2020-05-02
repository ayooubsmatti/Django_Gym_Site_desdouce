from django.contrib import admin
from .models import Entrenador,Milestone


class EntrenadorAdmin(admin.ModelAdmin):
    list_display=('entrenador_nombre','entrenador_descripcion','entrenador_url_img')

class MilestoneAdmin(admin.ModelAdmin) :
    list_display=('milestone_nombre','milestone_numero')

admin.site.register(Entrenador,EntrenadorAdmin)
admin.site.register(Milestone,MilestoneAdmin)
