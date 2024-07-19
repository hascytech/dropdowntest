from django import forms


class MatchPredictionForm(forms.Form):
    LEAGUES = [
        ('', 'Select League'),
        ('EPL', 'English Premier League'),
        ('LaLiga', 'La Liga'),
        ('SerieA', 'Serie A'),
        # Add other leagues as needed
    ]

    CLUBS = {
        'EPL': ['Manchester United', 'Liverpool', 'Chelsea', 'Arsenal'],
        'LaLiga': ['Barcelona', 'Real Madrid', 'Atletico Madrid', 'Sevilla'],
        'SerieA': ['Juventus', 'Inter Milan', 'AC Milan', 'Roma'],
        # Add clubs for other leagues
    }

    league = forms.ChoiceField(choices=LEAGUES, label='League')
    # home_team = forms.ChoiceField(choices=[], label='Home Team')
    home_team = forms.ChoiceField(choices=[('', 'Select home team')], label='Home Team')
    # away_team = forms.ChoiceField(choices=[], label='Away Team')
    away_team = forms.ChoiceField(choices=[('', 'Select away team')], label='Away Team')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['home_team'].choices = []
        # self.fields['away_team'].choices = []
        if 'data' in kwargs:
            data = kwargs['data']
            league = data.get('league')
            if league in self.CLUBS:
                team_choices = [(team, team) for team in self.CLUBS[league]]
                self.fields['home_team'].choices = [('', 'Select home team')] + team_choices
                self.fields['away_team'].choices = [('', 'Select away team')] + team_choices
            else:
                self.fields['home_team'].choices = [('', 'Select home team')]
                self.fields['away_team'].choices = [('', 'Select away team')]