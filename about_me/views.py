from django.shortcuts import render

# Create your views here.
def main_content(request):
    return render(request, "main_content.html")

def about_me(request):
    return render(request, "about_me.html")