from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

class FormBuilder(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f"title: {self.title} - id: {self.id}"


class FormField(models.Model):
    class FieldType:
        CHECKBOX = "checkbox"
        SHORT = "short"
        LONG = "long"
        RADIO = "radio"
        SELECT = "select"
        MULTI_SELECT = "multi_select"
        PHONE = "phone"
    form = models.ForeignKey(FormBuilder, on_delete=models.CASCADE)
    label = models.CharField(max_length=100, null=True, blank=True)
    placeholder = models.CharField(max_length=200, null=True, blank=True)
    order = models.PositiveIntegerField(default=0)
    field_type = models.CharField(max_length=50, choices=FieldType)
    required = models.BooleanField(default=False)


class FieldOption(models.Model):
    option = models.CharField(max_length=100)
    field = models.ForeignKey('FormField', related_name='options', on_delete=models.CASCADE)


class FormData(models.Model):
    form = models.ForeignKey(FormBuilder, on_delete=models.CASCADE)
    field = models.ForeignKey(FormField, on_delete=models.CASCADE)
    value = models.TextField()

class SelectOption(models.Model):
    option = models.CharField(max_length=100)
    field = models.ForeignKey('FormField', related_name='select_options', on_delete=models.CASCADE)