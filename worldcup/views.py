from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.template.loader import render_to_string
from django.shortcuts import render
from .models import worldcup_teams
from django.db.models import Max


# Create your views here.
def team_result(request, id):
    result = worldcup_teams.objects.get(id=id)
    return render(request, "worldcup/worldcup.html", {
        "country" : result.country,
        "captain" : result.captain,
        "is_top_3" : result.is_top_3,
        "goals" : result.goals,
        "stage" : result.stage
    })

def index(request):
    team_names = worldcup_teams.objects.all().order_by("goals")
    number_of_teams = team_names.count()
    max_goals = team_names.aggregate(Max("goals"))
    return render(request, "worldcup/index.html", {
        "team" : team_names,
        "number_of_teams" : number_of_teams,
        "max_goals" : max_goals
        })
    
def input(request):
    return render(request, "worldcup/input.html")

def insert(request):
    if request.method == "POST":
        user = request.POST["username"]
        return render(request, "worldcup/index.html", {
            "user": user
        })
    else:
        return render(request, "worldcup/index.html")