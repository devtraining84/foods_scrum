from datetime import datetime
import random
from django.shortcuts import render
from django.views import View
from jedzonko.models import Receipe, Plan, Recipeplan



class IndexView(View):

    def get(self, request):
        carousel = list(Receipe.objects.all())
        random.shuffle(carousel)
        receipe_s = carousel[0]
        carousel = carousel[1:3]

        return render(request, "index.html", {'carousel': carousel, 'receipe_s':receipe_s})


class DashboardView(View):

    def get(self, request):
        count_receipe = Receipe.objects.count()
        count_plan = Plan.objects.count()
        last_plan=Plan.objects.latest('created')
        last_plan_plan=Recipeplan.objects.filter(plan_id=last_plan)
        return render(request, 'dashboard.html', {'count_receipe': count_receipe, 'count_plan': count_plan, 'last_plan':last_plan, 'last_plan_plan':last_plan_plan,})



class Recipe_list(View):
    def get(self, request, id=0):
        recipis = Receipe.objects.order_by("votes")
        return render(request, "app-recipes.html", {'recipis':recipis})


def get_recipt_details(request,id):
    recipt_details = Receipe.objects.get(id=id)
    # dodano przyciks glosowania na przepis
    if request.method == 'GET':
        return render(request,'app-recipe-details.html',{'recipt_details':recipt_details})
    if request.method == 'POST':
        recipt_details.votes += 1
        recipt_details.save()
        return render(request,'app-recipe-details.html',{'recipt_details':recipt_details})

def add_plan(request):
    if request.method == "GET":
        return render(request, 'app-add-schedules.html')
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        if len(name) <1 or len(description) <1:
            message=(f"Wprowadz poprawne dane")
            return render(request, 'app-add-schedules.html',{'message':message})
        else:
            Plan.objects.create(name=name,description=description)
            # return do poprawy ma byc przekierowanie na /plan/<id>/details------------------
            return render(request,'app-details-schedules.html')
            # ---------------------------------------------------------------------------------------------




