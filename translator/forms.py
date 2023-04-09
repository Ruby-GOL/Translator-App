from django import forms

class TranslationForm(forms.Form):
    input_text = forms.CharField(widget=forms.Textarea)
    source_language = forms.CharField(max_length=10)
    target_language = forms.CharField(max_length=10)
    output_format = forms.ChoiceField(choices=[('text', 'Text'), ('audio', 'Audio')])
