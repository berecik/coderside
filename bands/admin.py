from django.contrib import admin
from .models import Band, Member, Musican


class BandAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ['name']


class MusicanAdmin(admin.ModelAdmin):
    pass


class MemberAdmin(admin.ModelAdmin):
    pass


admin.site.register(Band, BandAdmin)
admin.site.register(Musican, MusicanAdmin)
admin.site.register(Member, MemberAdmin)
