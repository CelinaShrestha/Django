from django.contrib import admin
from .models import Blog,Contact
# Register your models here.
admin.site.site_header="Blog Application"
admin.site.site_title="Mero Blog"
admin.site.index_title="Blog Admin"


class BlogAdmin(admin.ModelAdmin):
    list_display = ("__str__","title","user","subtitle","description",)
    fields = [("title","subtitle","user"),"description"]
    list_editable = "title","subtitle",
    search_fields = "title",


admin.site.register(Blog,BlogAdmin)
admin.site.register(Contact)