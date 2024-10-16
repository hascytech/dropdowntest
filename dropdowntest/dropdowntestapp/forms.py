from django import forms


class MatchPredictionForm(forms.Form):
    LEAGUES = [
        ('', 'Select League'),
        ('EPL', 'English Premier League'),
        ('LaLiga', 'La Liga'),
        ('SerieA', 'Serie A'),
        ('Bundesliga', 'Bundesliga'),
        ('Ligue1', 'Ligue 1'),
        ('NPL', 'Nigeria Premier League'),
        # Add other leagues as needed
    ]

    CLUBS = {
        'EPL': ['Arsenal', 'Aston Villa', 'Bournemouth', 'Brentford', 'Brighton & Hove Albion', 'Chelsea', 'Crystal \
                Palace', 'Everton', 'Fulham', 'Ipswich Town', 'Leicester City', 'Liverpool', 'Manchester City',
                'Manchester United', 'Newcastle United', 'Nottingham Forest', 'Southampton', 'Tottenham Hotspur',
                'West Ham United', 'Wolverhampton Wanderers'],
        'LaLiga': ['Alavés', 'Athletic Bilbao', 'Atlético Madrid', 'Barcelona', 'Celta Vigo', 'Espanyol', 'Getafe',
                   'Girona', 'Las Palmas', 'Leganés', 'Mallorca', 'Osasuna', 'Rayo Vallecano', 'Real Betis',
                   'Real Madrid', 'Real Sociedad', 'Sevilla', 'Valencia', 'Valladolid', 'Villarreal'],
        'SerieA': ['AC Milan', 'Atalanta', 'Bologna', 'Cagliari', 'Como', 'Fiorentina', 'Hellas', 'Genoa', 'Inter',
                   'Juventus', 'Lazio', 'Monza', 'Napoli', 'Parma', 'Roma', 'Torino', 'Udinese'],
        'Bundesliga': ['FC Augsburg', 'Union Berlin', 'VfL Bochum', 'Werder Bremen', 'Borussia Dortmund',
                       'Eintracht Frankfurt', 'SC Freiburg', '1. FC Heidenheim', 'TSG Hoffenheim', 'Holstein Kiel',
                       'RB Leipzig', 'Bayer Leverkusen', 'Mainz 05', 'Borussia Mönchengladbach', 'Bayern Munich',
                       'FC St. Pauli', 'VfB Stuttgart', 'VfL Wolfsburg', ],
        'Ligue 1': ['Angers', 'Auxerre', 'Brest', 'Le Havre', 'Lens', 'Lille', 'Lyon', 'Marseille', 'Monaco',
                    'Montpellier', 'Nantes', 'Nice', 'PSG', 'Reims', 'Rennes', 'Strasbourg', 'Saint-Étienne',
                    'Toulouse', ],
        'NPL': ['Abia Warriors', 'Akwa United', 'Bayelsa United', 'Bendel Insurance', 'El-Kanemi Warriors', 'Enugu \
                Rangers', 'Eyimba', 'Heartland', 'Ikorodu City', 'Kano Pillars', 'Katsina United', 'Kwara United',
                'Lobi Stars', 'Nasarawa United', 'Niger Tornadoes', 'Plateau United', 'Remo Stars', 'Rivers United',
                'Shooting Starts', 'Sunshine Stars'],
        # Add clubs for other leagues
    }

    league = forms.ChoiceField(
        choices=LEAGUES,
        label='League',
        widget=forms.Select(
            attrs={
                'class': 'form-control custom-select',  # Adds Bootstrap or custom CSS classes
                'id': 'id_league',  # You can specify a custom ID if needed
                'style': 'width: 100%;',  # Inline styles for better control
            }
        )
    )

    home_team = forms.ChoiceField(
        choices=[('', 'Select home team')],
        label='Home Team',
        widget=forms.Select(
            attrs={
                'class': 'form-control custom-select',  # Custom class
                'id': 'id_home_team',
                'style': 'width: 100%;',  # Inline styling to control width
            }
        )
    )

    away_team = forms.ChoiceField(
        choices=[('', 'Select away team')],
        label='Away Team',
        widget=forms.Select(
            attrs={
                'class': 'form-control custom-select',
                'id': 'id_away_team',
                'style': 'width: 100%;',
            }
        )
    )

    match_date = forms.DateField(
        label='Match Date',
        widget=forms.DateInput(
            attrs={
                'type': 'date',  # Ensures the input type is a date picker
                'class': 'form-control datepicker',  # Adds a datepicker class (if needed for external JS)
                'id': 'id_match_date',
                'style': 'width: 100%;',  # Control width
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

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

        else:
            # If form is not populated, set the default choices
            self.fields['home_team'].choices = [('', 'Select home team')]
            self.fields['away_team'].choices = [('', 'Select away team')]
