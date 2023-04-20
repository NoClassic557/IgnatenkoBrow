from django import forms


from .models import Services, Group, Blog


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = ['procedure', 'price', 'group']


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['name_blog', 'main_text']
