from django.shortcuts import render, redirect
from .forms import MovieForm
from .models import Movie

# Create your views here.
def index(request):
    movie_lists = Movie.objects.all()
    context = {
        'movie_lists': movie_lists,
    }
    return render(request, 'movies/index.html', context)

def detail(request, pk):
    movie_detail = Movie.objects.get(id=pk)
    context = {
        'movie_detail':movie_detail,
    }
    return render(request, 'movies/detail.html', context)

def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = MovieForm()
    context = {
        'form': form,
    }
    return render(request, 'movies/create.html', context)

def delete(request, pk):
    Movie.objects.get(id=pk).delete()
    return redirect('movies:index')

def update(request, pk):
    update_data = Movie.objects.get(id=pk)
    if request.method == 'POST':
        update_movie = MovieForm(request.POST, instance=update_data)
        if update_movie.is_valid():
            update_movie.save()
            return redirect('movies:detail', pk)
    else:
        update_movie = MovieForm(instance=update_data)

    context = {
        'update_movie':update_movie,
    }
    return render(request, 'movies/update.html', context)