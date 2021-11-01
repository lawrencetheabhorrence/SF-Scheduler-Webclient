from django import forms

class Sportsfest(forms.Form):
    days = forms.IntegerField(label='No. of Days for SF', min_value=1)
    timeslots = forms.IntegerField(label='No. of Timeslots per Day', min_value=1)
    timeslot_length = forms.IntegerField(label='Timeslot length in minutes', min_value=1)

class Game(forms.ModelForm):

