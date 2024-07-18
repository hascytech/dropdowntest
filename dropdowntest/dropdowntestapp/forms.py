from django import forms


class MatchPredictionForm(forms.Form):
    LEAGUES = [
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
    home_team = forms.ChoiceField(choices=[], label='Home Team')
    away_team = forms.ChoiceField(choices=[], label='Away Team')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['home_team'].choices = []
        self.fields['away_team'].choices = []
