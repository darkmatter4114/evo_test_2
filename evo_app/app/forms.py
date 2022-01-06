from django import forms

from evo_app.app.models import User, FullUser


class NameForm(forms.ModelForm):
    name = forms.CharField(label="Ім'я", max_length=100)

    # def clean_username(self):
    #     name = self.cleaned_data['name']
    #
    #     if User.objects.filter(name=name).exists():
    #         raise forms.ValidationError("User name already exist, please choose new one")
    #     return name

    class Meta:
        model = User
        fields = ['name']


class FullUserForm(forms.ModelForm):
    name = forms.CharField(label="Ім'я", max_length=30)
    lastName = forms.CharField(label="Фамілія", max_length=30)
    email = forms.CharField(label="Email", max_length=30)

    class Meta:
        model = FullUser
        fields = ['name', 'lastName', 'email']
