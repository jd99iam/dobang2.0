from django.shortcuts import render
from .models import Posts
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView
from django.shortcuts import redirect
from .models import User
# Create your views here.

class PostListView(ListView):
    model = Posts

class PostCreateView(CreateView):
    model = Posts
    fields = ['title','content']
    template_name = 'gallery/posts_create.html'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
             form.instance.save()
             return redirect('/')
        else  :
            return self.render_to_response({'form':form})

class PostDetailView(DetailView):
    model = Posts
    template_name = 'gallery/detail.html'

class PostDeleteView(DeleteView):
    model = Posts
    template_name = 'gallery/delete.html'
    success_url = '/'
