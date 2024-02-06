from django.forms import ModelForm, CharField, TextInput
from .models import Tag, Authors, Quotes


class TagForm(ModelForm):

    name = CharField(min_length=3, max_length=100, required=True, widget=TextInput())

    class Meta:
        model = Tag
        fields = ["name"]


class AuthorForm(ModelForm):

    fullname = CharField(min_length=3, max_length=60, required=True, widget=TextInput())
    born_date = CharField(min_length=3, max_length=50, widget=TextInput())
    born_location = CharField(min_length=3, max_length=100, widget=TextInput())
    description = CharField(widget=TextInput())

    class Meta:
        model = Authors
        fields = ["fullname", "born_date", "born_location", "description"]


class QuoteForm(ModelForm):

    quote = CharField(required=True, widget=TextInput())

    class Meta:
        model = Quotes
        fields = ["quote"]
        exclude = ["tags", "author"]
