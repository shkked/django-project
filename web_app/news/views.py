from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView


# Create your views here.
def news_home(request):
    news = Articles.objects.order_by("date")
    return render(request, 'news/news_home.html', {"news": news})

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/news-detail.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/news_create.html'
    
    form_class = ArticlesForm
    
    
class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'news/news_delete.html'


def news_create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'
    
    form = ArticlesForm()
    data = {
        'form': form, 
        'error': error  
    }
    return render(request, 'news/news_create.html', data)