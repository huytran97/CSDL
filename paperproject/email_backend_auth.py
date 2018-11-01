from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

class EmailBackendAuth(object):

    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            print(user)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            pass
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None