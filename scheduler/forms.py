from django import forms

class Sportsfest(forms.Form):
    days = forms.IntegerField(label='No. of Days for SF', min_value=1)
    timeslots = forms.IntegerField(label='No. of Timeslots per Day', min_value=1)
    timeslot_length = forms.IntegerField(label='Timeslot length in minutes', min_value=1)

class Game(forms.Form):
    name = forms.CharField(label='Name of game', max_length=300)
    n_timeslots = forms.IntegerField(label='Number of Timeslots per Round', min_value=1)
    priority = forms.Select(choices=[(a,a) for a in ['Major','Minor','Junior']])
    categories = forms.IntegerField('Number of Categories', min_value=1)
