from django import forms

from Fruitipedia.fruit.models import Profile, Fruit


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class CreateProfileForm(BaseProfileForm):
    class Meta(BaseProfileForm.Meta):
        fields = ['first_name', 'last_name', 'email', 'password']
        labels = {
            'first_name': False,
            'last_name': False,
            'email': False,
            'password': False
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
        }
        password = forms.PasswordInput()


class EditProfileForm(BaseProfileForm):
    class Meta(BaseProfileForm.Meta):
        fields = ['first_name', 'last_name', 'image_url', 'age']
        labels = {
            'first_name': "First Name",
            'last_name': "Last Name",
            'image_url': "Image URL",
            'age': "Age",
        }


class BaseFruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'


class CreateFruitForm(BaseFruitForm):
    class Meta(BaseFruitForm.Meta):
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Fruit Name'}),
            'image_url': forms.TextInput(attrs={'placeholder': 'Fruit Image URL'}),
            'description': forms.TextInput(attrs={'placeholder': 'Fruit Description'}),
            'nutrition': forms.TextInput(attrs={'placeholder': 'Nutrition Info'}),
        }

        labels = {
            'name': '',
            'image_url': '',
            'description': '',
            'nutrition': '',
        }


class EditFruitPage(BaseFruitForm):
    class Meta(BaseFruitForm.Meta):
        labels = {
            'name': 'Name:',
            'image_url': 'Image URL:',
            'description': 'Description:',
            'nutrition': 'Nutrition:',
        }


class DeleteFruitForm(BaseFruitForm):
    class Meta(BaseFruitForm.Meta):
        exclude = ['nutrition']
        labels = {
            'image_url': 'Image URL',
        }
