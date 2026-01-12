from django.shortcuts import render

posts = [
    {
        "title":"Blog Post 1",
        "content": "Be not overcome with evil, but overcome evil with good",
        "date_posted": "January 12, 2026"
    },
    {
        "title":"Blog Post 2",
        "content": "Pour your heart in to IT",
        "date_posted": "January 12, 2026"
    }
]

# Create your views here.
def home(request):
    # return HttpResponse('<h1>Blog Home</h1>')
    context = {
        "posts":posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')

