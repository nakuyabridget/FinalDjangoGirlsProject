#from django.models import UserProfileForm
from django.contrib.auth.models import User
from django import forms
from .models import Post
from django.db.models import Q

import re#This the regular expressions library.
from django.core.exceptions import ObjectDoesNotExist

#class UserForm(forms.ModelForm):
	#password = forms.CharField(widget=forms.PasswordInput())

	#class Meta:
		#model = UserForm
		#fields = ('username','email','password')
class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=30)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Password',
                          widget=forms.PasswordInput())
    password2 = forms.CharField(label='Password (Again)',
                        widget=forms.PasswordInput())
    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2:
                return password2
        raise forms.ValidationError('Passwords do not match.')

class LoginForm(forms.Form):
	username = forms.CharField(label='Username', max_length = 30)
	password = forms.CharField(label = ' Password', widget = forms.PasswordInput())


class AddPostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ('author','title','text')

    #def clean_username(self):
    	#username = self.cleaned_data['username']

    	#if not re.search(r'^\w+$', username):

        	#raise forms.ValidationError('Username can only contain alphanumeric characters and the underscore.')
        #try:
        	#User.objects.get(username=username)
        #except ObjectDoesNotExist:

    		#return username

   		#raise forms.ValidationError('Username is already taken.')


class SearchForm(forms.Form):
    class Meta:
        search_fields = ('^name', 'description', 'specifications', '=id') 

        # assumes a fulltext index has been defined on the fields
        # 'name,description,specifications,id'
        fulltext_indexes = (
            ('name', 2), # name matches are weighted higher
            ('name,description,specifications,id', 1),
        )

    """ 
    A custom addition - the absence of a prepare_category method means
    the query will search for an exact match on this field.
    """
    