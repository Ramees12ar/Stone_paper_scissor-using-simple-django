from django.shortcuts import render
import json
from django.http import HttpResponse,JsonResponse

# Create your views here.

def home(request):
	return render(request,"home/index.html",{})
com=0
ply=0
def game(request):
	global com,ply
	val=request.POST.get("element")
	#print(val)
	import random
	data=["stone","paper","scissor"]
	pc=random.choice(data)
	if(val==pc):
		result="tie"
		return render(request,"home/index.html",{"result":result,"pc":pc,"ply":ply,"val":val,"com":com})
	elif(val=="stone" and pc=="paper"):
		com+=1
		result="Computer got 1 point"
		return render(request,"home/index.html",{"result":result,"pc":pc,"ply":ply,"val":val,"com":com})
	elif(val=="paper" and pc=="scissor"):
		result="computer got 1 point"
		com+=1
		return render(request,"home/index.html",{"result":result,"pc":pc,"ply":ply,"val":val,"com":com})
	elif(val=="scissor" and pc=="stone"):
		result="computer got 1 point"
		com+=1
		return render(request,"home/index.html",{"result":result,"pc":pc,"ply":ply,"val":val,"com":com})
	else:
		result="you got 1 point"
		ply+=1
		return render(request,"home/index.html",{"result":result,"pc":pc,"ply":ply,"val":val,"com":com})
def quite(request):
	a=request.POST.get("plyr")
	b=request.POST.get("com")
	global com,ply
	com=0
	ply=0
	if(int(a)==int(b)):
		return HttpResponse("<script>alert('Match tied');window.location.href='/index/';</script>")
	elif(int(a)>int(b)):
		return HttpResponse("<script>alert('Congrats...You won the game');window.location.href='/index/';</script>")
	else:
		return HttpResponse("<script>alert('Better Luck next time... PC won the game');window.location.href='/index/';</script>")
def index(request):
	return render(request,"home/index.html",{})
