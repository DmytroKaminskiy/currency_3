from account.models import User, Avatar

from django.contrib import admin


class AvatarInline(admin.TabularInline):
# class AvatarInline(admin.StackedInline):
    model = Avatar
    extra = 0


class UserAdmin(admin.ModelAdmin):
    inlines = (AvatarInline, )


class AvatarAdmin(admin.ModelAdmin):
    raw_id_fields = ['user', ]
    list_display = ('id', 'user')
    list_select_related = ['user']  # Avatar.objects.select_related('user')
    # readonly_fields = ('user', )


admin.site.register(User, UserAdmin)
admin.site.register(Avatar, AvatarAdmin)

"""
User
list_display = [
list_filter = [
readonly_fields = (
search_fields = 

Create new permission
User - full_edit

"""