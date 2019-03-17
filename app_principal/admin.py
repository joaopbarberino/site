from django import forms
from django.contrib import admin

from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User, Livro

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email','first_name')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("As senhas não combinam !")
        return password2
    
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email','first_name','last_name','is_staff','is_superuser','is_active','last_login')

    def clean_password(self):
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('first_name','last_name','email')
    list_filter = ('is_superuser',)
    fieldsets = (
        (None,{'fields':('email', 'password')}),
        ('Personal info',{'fields':('first_name', 'last_name')}),
        ('Permissions',{'fields':('is_superuser',)}),
    )

    add_fieldsets = (
        (None,{
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'password1', 'password2')
        })
    )

    search_fields = ('first_name',)
    ordering = ('first_name',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.register(Livro)
admin.site.unregister(Group)
