from django.contrib import admin
from .models import Post,Comment,Neighbourhood,Business,Profile,Location,Category
# from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
# Registering Models
# admin.site.register(User, UserAdmin)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Neighbourhood)
admin.site.register(Business)
admin.site.register(Profile)
admin.site.register(Location)
admin.site.register(Category)