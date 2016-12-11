#-*- coding: utf-8 -*-
from django import forms

class CreateGroup(forms.Form):
   name = forms.CharField(max_length=30)


class AddMember(forms.Form):
   email = forms.EmailField()