from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Article, Contact
from .forms import ContactUsForm

# Create your views here.

def index(request):
    articles = Article.objects.all()[:3]
    if request.method == 'POST':
        contact_form = ContactUsForm(request.POST)
        if contact_form.is_valid():
            cd = contact_form.cleaned_data
            Contact.objects.create(first_name=cd['first_name'],last_name=cd['last_name'],email=cd['email'],message=cd['message'])
            return redirect('journal:index')
    else:
        contact_form = ContactUsForm()
    return render(request, 'app/index.html', {'articles': articles, 'contact_form': contact_form})

def article_detail(request, category, slug):
    if not category==None and not slug==None:
        article = get_object_or_404(Article, category=category, slug=slug)
        return render(request, 'app/detail.html', {'article': article})
    else:
        return HttpResponse('No such article!')

