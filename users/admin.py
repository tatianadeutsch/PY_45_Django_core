from django.contrib import admin

from users.models import User

admin.site.register(User)

# from users.models import Users


# @admin.register(Users)
# class UsersAdmin(admin.ModelAdmin):
#     list_display = (
#         "name",
#         "nickname",
#         "email",
#         "password",
#         "password_confirm",
#         "phone",
#         "date_of_birth",
#     )
