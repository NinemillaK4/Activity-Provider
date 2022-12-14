from django import forms
from django.forms.widgets import RadioSelect


class QuestionForm(forms.Form):
    def __init__(self, question, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        choice_list = [x for x in question.get_answers_list()]
        self.fields["answers"] = forms.ChoiceField(choices=choice_list, widget=RadioSelect)

class startConf(forms.Form):
    resume = forms.CharField(max_length=500,help_text="Resumo")
    url = forms.CharField(max_length=500,help_text="Url")
    


