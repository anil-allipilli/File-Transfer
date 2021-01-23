from rest_framework import permissions


class IsItSharedWithUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print("hello, object")
        # returns false with if the product is not created by the user and not shared with user
        print(request.user)
        print(obj.product_users.all())
        print(request.user not in obj.product_users.all())
        # print(obj.owner)
        if (request.user not in obj.product_users.all()) and (
            request.user != obj.owner
        ):
            return False
        else:
            return True
