from rest_framework.permissions import BasePermission, IsAuthenticated


class IsConnectedUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsPerson(IsAuthenticated):
    def has_permission(self, request, view):
        if super().has_permission(request, view):
            return hasattr(request.user, 'person')
        return False


class IsDogOwner(IsPerson):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user.person
