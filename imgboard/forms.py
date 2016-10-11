from django import forms

class PostForm(forms.Form):
	post_text = forms.CharField(label='Enter your message here', max_length=300)
	picture = forms.ImageField(label='', required=False)
