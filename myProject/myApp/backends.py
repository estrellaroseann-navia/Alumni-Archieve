from django.contrib.auth.backends import BaseBackend
from .models import RegisteredAlumni

class EmailBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        try:
            user = RegisteredAlumni.objects.get(email=email)
            if user.check_password(password):
                return user
        except RegisteredAlumni.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return RegisteredAlumni.objects.get(pk=user_id)
        except RegisteredAlumni.DoesNotExist:
            return None
