from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        '''Кастомная функция для разрешения доступа к просмотру данных'''
        if request.method in permissions.SAFE_METHODS:#если метод безопасный
            return True#даем доступ всем пользователям

        return bool(request.user and request.user.is_staff)


class IsOwnerOrReadOnly(permissions.BasePermission):
    '''Кастомная функция для контретного объекта, разрешение на уровне одной записи'''
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user
