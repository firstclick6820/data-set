from django.contrib import admin



from .models import AffiliatePrograms



class AffiliateAdmin(admin.ModelAdmin):
    list_display = ['service']
    
admin.site.register(AffiliatePrograms, AffiliateAdmin)