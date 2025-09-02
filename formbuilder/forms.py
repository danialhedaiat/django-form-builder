from django import forms

from form_builder.models import FormBuilder


class FormBuilderForm(forms.ModelForm):
    title = forms.CharField(max_length=200, label='Form Title')
    description = forms.CharField(widget=forms.Textarea, label='Form Description', required=False)
    object_id = forms.IntegerField(label='Object ID')
    content_type = forms.CharField(max_length=100, label='Content Type')

    class Meta:
        model = FormBuilder
        fields = ['title', 'description', 'object_id', 'content_type']
