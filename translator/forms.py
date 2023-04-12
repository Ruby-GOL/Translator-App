from django import forms

class TranslationForm(forms.Form):
    input_text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter text to translate'}), required=False)
    target_language = forms.ChoiceField(choices=[('en', 'English'), ('es', 'Spanish'), ('fr', 'French'), ('de', 'German')], initial='en')
    audio_file = forms.FileField(required=False)

