from django.shortcuts import redirect, render
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        article_create_form = ArticleForm(request.POST)
        if article_create_form.is_valid():
            article = article_create_form.save(commit=False)
            article.user = request.user
            article.save()
            messages.success(request, '글 작성이 완료되었습니다.')
            return redirect('articles:index')
    else:
        article_create_form = ArticleForm()
    context = {
        'article_create_form': article_create_form,
    }
    return render(request, 'articles/form.html', context)

def comments_create(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comment_form = CommentForm(request.POST)
    if request.method == 'POST':
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
    return redirect('articles:article_detail', article_pk)

def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('articles:article_detail', article_pk)
