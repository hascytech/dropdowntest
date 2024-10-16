from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render

from .forms import MatchPredictionForm
from .prediction import predict_winner

# from .prediction import predict_winner  # Import your prediction function


def get_clubs(request):
    league = request.GET.get('league')

    # Logic to fetch clubs based on the selected league
    clubs_dict = {
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
        # Add more leagues and their respective clubs
    }

    # Get clubs for the selected league
    clubs = clubs_dict.get(league, [])

    return JsonResponse({'clubs': clubs})


def index(request):
    if request.method == 'POST':
        form = MatchPredictionForm(request.POST)
        if not form.is_valid():
            print(form.errors)
            print(form)

        if True:
            league = form.data.get('league')
            home_team = form.data.get('home_team')
            away_team = form.data.get('away_team')
            match_date = form.data.get('match_date')

            # Store form data in session
            request.session['league'] = league
            request.session['home_team'] = home_team
            request.session['away_team'] = away_team
            request.session['match_date'] = match_date

            # Redirect to the result view
            return HttpResponseRedirect('/result/')
    else:
        form = MatchPredictionForm()

    return render(request, 'dropdowntestapp/index.html', {'form': form})


def result(request):
    # Retrieve form data from session
    league = request.session.get('league')
    home_team = request.session.get('home_team')
    away_team = request.session.get('away_team')
    match_date = request.session.get('match_date')
    prediction = predict_winner(home_team, away_team)

    # print(prediction)

    return render(request, 'dropdowntestapp/result.html', {
        'home_team_name': home_team,
        'away_team_name': away_team,
        'date_match': match_date,
        'league': league,
        'final_result': prediction,  # Placeholder result
    })


def about(request):
    return render(request, 'dropdowntestapp/about.html')


def privacy(request):
    return render(request, 'dropdowntestapp/privacy.html')


def terms(request):
    return render(request, 'dropdowntestapp/terms.html')


def contact(request):
    return render(request, 'dropdowntestapp/contact.html')
