from django.http import HttpResponse
from django.shortcuts import render

def test():
    return HttpResponse ("Hello")

def Aboutus(request):
    return render(request,"aboutus.html")

def Contectus(request):
    return render(request,"contectus.html")

def Home(request):
    return render(request,"home.html")

def Movies(request):
    return render(request,"movies.html")

def Shows(request):
    return render(request,"shows.html")

def News(request):
    return render(request,"news.html")

def Recipes(request):
    ingredient=["maggie","tomato"]
    data = {"name":"maggie","time":20,"ingredient":ingredient}
    return render(request,"recipe.html",data)

def Team(request):
    players=["rajat patidar","Phil Salt","Tim David","Devdutt Padikkal","Krunal Pandya","Romario Shepherd","Bhuvneshwar Kumar","Josh Hazlewood","Yash Dayal","Suyash Sharma"]
    data = {"captain":"virat kohli","trophy":1,"playerlist":players}
    return render(request,"team.html",data)

def IPL(request):
    teams=["RCB","CSK","MI","PBKS","KKR","SRH","DC","GT","LSG","RR"]
    data={"teams":teams,"trophy":5}
    return render(request,"ipl.html",data)