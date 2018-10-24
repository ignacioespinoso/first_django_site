from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone
from django.views import generic
from .models import Post

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_posts'

    def get_queryset(self):
        return Post.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'

    def get_queryset(self):
        return Post.objects.filter(pub_date__lte=timezone.now())

