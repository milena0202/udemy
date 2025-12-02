from rest_framework.permissions import BasePermission

class StudentPermission(BasePermission):
     def has_permission(self, request, view):
        return request.user.role == 'клиент'


class TeacherPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'преподаватель'