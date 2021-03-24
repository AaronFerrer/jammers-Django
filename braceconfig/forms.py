from django import forms

class BraceOne(forms.Form):
    brace_one = forms.IntegerField(help_text="")

class BraceTwo(forms.Form):
    brace_two = forms.IntegerField(help_text="")

class BraceThree(forms.Form):
    brace_three = forms.IntegerField(help_text="")

class BraceFour(forms.Form):
    brace_four = forms.IntegerField(help_text="")

class BraceFive(forms.Form):
    brace_five = forms.IntegerField(help_text="")

class BraceSix(forms.Form):
    brace_six = forms.IntegerField(help_text="")
    


'''
from braceconfig.models import RxInstance

class rxForm(forms.ModelForm):

    class Meta:
        model=RxInstance
        fields=['brace_one','brace_two','brace_three','brace_four','brace_five','brace_six']
        widgets = {
            'brace_one':   forms.IntegerField(help_text=""),
            'brace_two':   forms.IntegerField(help_text=""),
            'brace_three': forms.IntegerField(help_text=""),
            'brace_four':  forms.IntegerField(help_text=""),
            'brace_five':  forms.IntegerField(help_text=""),
            'brace_six':   forms.IntegerField(help_text="")

        }
'''