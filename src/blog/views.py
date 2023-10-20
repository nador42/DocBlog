from django.shortcuts import render
def index(request):
    return render(request,"blog/index.html")
def article(request,num_art):
    if num_art in ["01","02","03"]:
        return render(request,f"blog/article_{num_art}.html")
    return render(request,"blog/article_nom_trouve.html")


