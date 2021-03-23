# Create custom permissions

from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    message = "You must be the owner of this object."

    def has_permissions(self, request, obj):
        if request.method in SAFE_METHODS:
            return True
        return False


    def has_object_permission(self, request, view, obj):
        #my_safe_method = ['PUT']
        if request.method in SAFE_METHODS:
            return True
        return obj.user_id == request.user_id
