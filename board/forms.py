from django import forms
from .models import SchoolRecord, TargetUniv


class SchoolRecordForm(forms.ModelForm):
    firstFirst = forms.FloatField(label="1학년 1학기", required=False, max_value=10, min_value=0,
      widget=forms.NumberInput(
          attrs={
            'id': 'form_firstFirst',
            'step': "0.01",
            'placeholder': '',
          }))
    firstSecond = forms.FloatField(label="1학년 2학기", required=False, max_value=10, min_value=0,
      widget=forms.NumberInput(
          attrs={
            'id': 'form_firstSecond',
            'step': "0.01",
            'placeholder': '',
          }))
    secondFirst = forms.FloatField(label="2학년 1학기", required=False, max_value=10, min_value=0,
      widget=forms.NumberInput(
      attrs={'id': 'form_secondFirst',
             'step': "0.01",
            'placeholder': '',
            }))
    secondSecond = forms.FloatField(label="2학년 2학기", required=False, max_value=10, min_value=0,
      widget=forms.NumberInput(
          attrs={'id': 'form_secondSecond',
                 'step': "0.01",
                 'placeholder': '',
                }))
    thirdFirst = forms.FloatField(label="3학년 1학기", required=False, max_value=10, min_value=0,
      widget=forms.NumberInput(
          attrs={
            'id': 'form_thirdFirst',
            'step': "0.01",
            'placeholder': '',
          }))
    thirdSecond = forms.FloatField(label="3학년 2학기", required=False, max_value=10, min_value=0,
      widget=forms.NumberInput(
          attrs={
            'id': 'form_thirdSecond',
            'step': "0.01",
            'placeholder': '',
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
    
    class Meta:
        model = TargetUniv
        fields = [
            'order',
            'univ',
            'major',
            'applyType'
        ]
