from django import forms
from .models import SchoolRecord, Record, Test, TargetUniv, Question


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
        

class RecordForm(forms.ModelForm):
    file = forms.FileField(label='')
    class Meta:
        model = Record
        fields = [
            'file',
        ]

    def __init__(self, *args, **kwargs):
        super(RecordForm, self).__init__(*args, **kwargs)
        self.fields['file'].required = False


class TestForm(forms.ModelForm):
    # month = forms.IntegerField()
    koreanPoint = forms.IntegerField(label="국어 표준점수", widget=forms.NumberInput(attrs={'style': 'width:80px'}))
    koreanPercent = forms.IntegerField(label="국어 백분위", widget=forms.NumberInput(attrs={'style': 'width:80px'}))
    # koreanGrade = forms.IntegerField(label="국어 등급")
    mathPoint = forms.IntegerField(label="수학 표준점수", widget=forms.NumberInput(attrs={'style': 'width:80px'}))
    mathPercent = forms.IntegerField(label="수학 백분위", widget=forms.NumberInput(attrs={'style': 'width:80px'}))
    # mathGrade = forms.IntegerField(label="수학 등급")
    englishPoint = forms.IntegerField(label="영어 표준점수", widget=forms.NumberInput(attrs={'style': 'width:80px'}))
    englishPercent = forms.IntegerField(label="영어 백분위", widget=forms.NumberInput(attrs={'style': 'width:80px'}))
    # englishGrade = forms.IntegerField(label="영어 등급")
    # tamguFirstName = forms.CharField(max_length=20)
    # tamguFirstGrade = forms.IntegerField(label="탐구1 등급")
    tamguFirstPoint = forms.IntegerField(label="탐구1 표준점수", widget=forms.NumberInput(attrs={'style': 'width:80px'}))
    tamguFirstPercent = forms.IntegerField(label="탐구1 백분위", widget=forms.NumberInput(attrs={'style': 'width:80px'}))
    # tamguSecondName = forms.CharField(max_length=20)
    # tamguSecondGrade = forms.IntegerField(label="탐구2 등급")
    tamguSecondPoint = forms.IntegerField(label="탐구2 표준점수", widget=forms.NumberInput(attrs={'style': 'width:80px'}))
    tamguSecondPercent = forms.IntegerField(label="탐구2 백분위", widget=forms.NumberInput(attrs={'style': 'width:80px'}))
    # foreignName = forms.CharField(max_length=20, label="제2외국어")
    # foreignGrade = forms.IntegerField(label="제2외국어 등급")
    foreignPoint = forms.IntegerField(label="제2외국어 표준점수", widget=forms.NumberInput(attrs={'style': 'width:80px'}))
    foreignPercent = forms.IntegerField(label="제2외국어 백분위", widget=forms.NumberInput(attrs={'style': 'width:80px'}))
    
    class Meta:
        model = Test
        # input을 만들 칼럼 값을 list로 만들어 넣어준다.
        fields = [
                  # 'user',
                  'year',
                  'month',
                  'koreanPoint',
                  'koreanPercent',
                  'koreanGrade',
                  'mathPoint',
                  'mathPercent',
                  'mathGrade',
                  'englishPoint',
                  'englishPercent',
                  'englishGrade',
                  'tamguFirstName',
                  'tamguFirstGrade',
                  'tamguFirstPoint',
                  'tamguFirstPercent',
                  'tamguSecondName',
                  'tamguSecondGrade',
                  'tamguSecondPoint',
                  'tamguSecondPercent',
                  'foreignName',
                  'foreignGrade',
                  'foreignPoint',
                  'foreignPercent',
                  ]
        
    def __init__(self, *args, **kwargs):
        super(TestForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        self.fields['koreanGrade'].widget.attrs['width'] = 80
        self.fields['mathGrade'].widget.attrs['width'] = 80
        self.fields['englishGrade'].widget.attrs['width'] = 80
        self.fields['tamguFirstName'].widget.attrs['width'] = 80
        self.fields['tamguFirstGrade'].widget.attrs['width'] = 80
        self.fields['tamguSecondName'].widget.attrs['width'] = 80
        self.fields['tamguSecondGrade'].widget.attrs['width'] = 80
        self.fields['foreignName'].widget.attrs['width'] = 80
        self.fields['foreignGrade'].widget.attrs['width'] = 80

        
class TargetUnivForm(forms.ModelForm):
    # order = forms.IntegerField()
    univ = forms.CharField(max_length=30, required=False)
    major = forms.CharField(max_length=30, required=False)
    applyType = forms.CharField(max_length=30, required=False)
    
    class Meta:
        model = TargetUniv
        fields = [
            'order',
            'univ',
            'major',
            'applyType'
        ]

        
class QuestionForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': '질문 사항을 입력하세요'}),
                             label=(''),
                             required=False)
    
    class Meta:
        model = Question
        fields = [
            'content',
        ]
        
class FeedbackForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': '피드백 사항을 입력하세요'}),
                             label=(''),
                             required=False)
    
    class Meta:
        model = Question
        fields = [
            'content',
        ]
