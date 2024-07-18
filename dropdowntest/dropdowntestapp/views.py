from django.http import JsonResponse
from django.shortcuts import render

from .forms import MatchPredictionForm


def get_clubs(request):
    league = request.GET.get('league')
    # Replace this with your logic to fetch clubs based on the selected league
    clubs = ['Club A', 'Club B', 'Club C']  # Example clubs
    return JsonResponse({'clubs': clubs})


def index(request):
    form = MatchPredictionForm()

    if request.method == 'POST':
        form = MatchPredictionForm(request.POST)
        if form.is_valid():
            league = form.cleaned_data['league']
            home_team = form.cleaned_data['home_team']
            away_team = form.cleaned_data['away_team']
            # Add logic to predict the match winner
            prediction = 'Predicted Winner'
            return render(request, 'dropdowntestapp/index.html', {'form': form, 'prediction': prediction})

    return render(request, 'dropdowntestapp/index.html', {'form': form})


def about(request):
    return render(request, 'dropdowntestapp/about.html')


def privacy(request):
    return render(request, 'dropdowntestapp/privacy.html')


def terms(request):
    return render(request, 'dropdowntestapp/terms.html')


def contact(request):
    return render(request, 'dropdowntestapp/contact.html')
