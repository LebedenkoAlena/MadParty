from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

User = get_user_model()


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password"]


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password',)
