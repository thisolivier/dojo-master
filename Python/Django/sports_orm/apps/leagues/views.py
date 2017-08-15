from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	LeaguesNew = Team.objects.filter(location="Atlanta").values('league')
	for my_le in LeaguesNew:
		querySection = League.objects.filter(id=my_le['league']).values('name')
		try:
			queryResult | querySection
		except:
			queryResult = querySection
	
	context = {
		# "leagues": Leagues.objects.all(),
		# "teams": Team.objects.all().order_by('-team_name')
		"players": Player.objects.all().filter(first_name__regex=r'Alexander|Wyatt')
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")