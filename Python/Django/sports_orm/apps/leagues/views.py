from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Count

from . import team_maker

def index(request):
	bad_teams = Player.objects.get(first_name="Samuel", last_name="Evans").all_teams.all().values_list('id', flat=True)
	context = {
		# "leagues": leagues,
		"teams": Team.objects.all().filter(id__in=bad_teams),
		"players": Player.objects.filter(last_name='Flores')
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")