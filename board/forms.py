from django import forms
from .models import SchoolRecord


class SchoolRecordForm(forms.ModelForm):
    firstFirst = forms.FloatField(required=False, max_value=10, min_value=0,
      widget=forms.NumberInput(
          attrs={
            'id': 'form_firstFirst',
            'step': "0.01"
          }))
    firstSecond = forms.FloatField(required=False, max_value=10, min_value=0,
      widget=forms.NumberInput(
          attrs={
            'id': 'form_firstSecond',
            'step': "0.01"
          }))
    secondFirst = forms.FloatField(required=False, max_value=10, min_value=0,
      widget=forms.NumberInput(
          attrs={'id': 'form_secondFirst',
                 'step': "0.01"
                }))
    secondSecond = forms.FloatField(required=False, max_value=10, min_value=0,
      widget=forms.NumberInput(
          attrs={'id': 'form_secondSecond',
                 'step': "0.01"
                }))
    thirdFirst = forms.FloatField(required=False, max_value=10, min_value=0,
      widget=forms.NumberInput(
          attrs={
            'id': 'form_thirdFirst',
            'step': "0.01"
          }))
    thirdSecond = forms.FloatField(required=False, max_value=10, min_value=0,
      widget=forms.NumberInput(
          attrs={
            'id': 'form_thirdSecond',
            'step': "0.01"
          }))
    
    class Meta:
        model = SchoolRecord
        # input을 만들 칼럼 값을 list로 만들어 넣어준다.
        fields = [
                  'firstFirst',
                  'firstSecond',
                  'secondFirst',
                  'secondSecond',
                  'thirdFirst',
                  'thirdSecond'
                  ]

class TargetUnivForm(forms.ModelForm):
    order = forms.IntegerField()
    univ = forms.CharField(max_length=30)
    major = forms.CharField(max_length=30)
    applyType = forms.CharField(max_length=30)

        