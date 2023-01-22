from django.contrib import admin
from .models import worldcup_teams, captain, club
# Register your models here.

class clubAdmin(admin.ModelAdmin):
    list_display = {"league", "cup"}

class captainAdmin(admin.ModelAdmin):
    list_display = {"first_name", "last_name"}

class worldcup_teamsAdmin(admin.ModelAdmin):
    list_filter = ("goals", "country")
    list_display = ("country", "stage")

admin.site.register(worldcup_teams, worldcup_teamsAdmin)
admin.site.register(captain)
admin.site.register(club)
