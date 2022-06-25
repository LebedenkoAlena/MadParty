from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

User = get_user_model()


class PlaceholderWidgetFormMixin(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"placeholder": field.label, "type": field.widget.input_type, "name": name})


class CreateUserForm(PlaceholderWidgetFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]


class UserLoginForm(PlaceholderWidgetFormMixin, AuthenticationForm):
    class Meta:
        model = User
