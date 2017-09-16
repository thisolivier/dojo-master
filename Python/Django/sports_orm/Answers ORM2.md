# SPORTS ORM 2
1. ...all teams in the Atlantic Soccer Conference

2. ...all (current) players on the Boston Penguins

3. ...all (current) players in the International Collegiate Baseball Conference

4. ...all (current) players in the American Conference of Amateur Football with last name "Lopez"

    ### From views
	```python
    teams_new = League.objects.get(name="American Conference of Amateur Football").teams.all()
	for team in teams_new:
		for player in team.curr_players.all().filter(last_name = "Lopez"):
			try:
				queryset.append(player)
			except:
				queryset = [player]
    ```

    ```
    context = {
		# "leagues": League.objects.all(),
		# "teams": Team.objects.all(),
		"players": queryset
	}
    ```

    ### Output

    1. Levi Lopez
    2. Isabella Lopez
	

5. ...all football players

    ### From views
	```python
	leagues_new = League.objects.filter(sport="Football")

	for league in leagues_new:
		for team in league.teams.all():
			for player in team.curr_players.all():
				try:
					queryset.append(player)
				except:
					queryset = [player]
	
	context = {
		# "leagues": League.objects.all(),
		# "teams": Team.objects.all(),
		"players": queryset
	}
	return render(request, "leagues/index.html", context)
    ```

	### Output
	1. Charles Campbell
	2. Aiden Hernandez
	3. Jackson Perry
	-
	67. Noah Brooks

6. ...all teams with a (current) player named "Sophia"

	### Views
	```python
	players_new = Player.objects.filter(first_name='Sophia')
	teams = []
	for player in players_new:
		team_name_full = player.curr_team.location + " " +player.curr_team.team_name
		teams.append(team_name_full)
	```

	### Template
	```html
	{% for team in teams %}
				<li>{{team}}</li>
	```

	### Results
	1. Mexico City Cave Spiders
	2. Houston Hornets
	3. Wisconsin Devils


7. ...all leagues with a (current) player named "Sophia"

	### Views
	```python
	players_new = Player.objects.filter(first_name='Sophia')
	leagues = []
	for player in players_new:
		leagues.append(player.curr_team.league.name)
	```

	### Answers
	1. International Collegiate Baseball Conference
	2. Atlantic Federation of Basketball Athletics
	3. Atlantic Amateur Field Hockey League

8. ...everyone with the last name "Flores" who DOESN'T (currently) play for the Washington Roughriders

	### Views
	```python
	bad_team = Team.objects.get(team_name="Roughriders", location="Washington")		
	
	context = {
		# "leagues": leagues,
		# "teams": teams
		"players": Player.objects.filter(last_name='Flores').exclude(curr_team=bad_team)
	```

9. ...all teams, past and present, that Samuel Evans has played with

10. ...all players, past and present, with the Manitoba Tiger-Cats

11. ...all players who were formerly (but aren't currently) with the Wichita Vikings

12. ...every team that Jacob Gray played for before he joined the Oregon Colts

13. ...everyone named "Joshua" who has ever played in the Atlantic Federation of Amateur Baseball Players

14. ...all teams that have had 12 or more players, past and present. (HINT: Look up the Django annotate function.)

15. ...all players and count of teams played for, sorted by the number of teams they've played for