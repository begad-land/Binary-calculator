
from django import forms

operation_choices = [
    ('B', 'Binary To Decimal'),
    ('D', 'Decimal To Binary'),
]


class BinaryForm(forms.Form):
    number = forms.CharField(max_length=8 , label = 'insert you number')
    operation = forms.ChoiceField(choices= operation_choices , label = "Operation")

