from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Blog, Category, Comment
from .forms import BlogForm, CommentForm
from django.db.models import Q
from django.urls import reverse_lazy




class HomePageView(ListView):
    model = Blog
    template_name = 'index.html'
    context_object_name = 'blogs'

    def get_context_data(self, **kwargs):

        context = super(HomePageView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['read_count'] = 'read_count'
        context['creation_time'] = 'creation_time'

        return context

    def get_queryset(self, *args, **kwargs):

        category = self.request.GET.get('category')
        creation_time = self.request.GET.get('creation_time')
        read_count = self.request.GET.get('-read_count')
        filtered_value = self.request.GET.get('filtered_value')
        if category:
            queryset = Blog.objects.filter(category__name = category)
        elif creation_time:
            queryset = Blog.objects.order_by('-read_count')
        elif read_count:
            queryset = Blog.objects.order_by('read_count')
        elif filtered_value:
            queryset = Blog.objects.filter(Q(header__icontains = filtered_value) | Q(text__icontains = filtered_value) )
            print(queryset)
        else:
            queryset = Blog.objects.all()
        return queryset

class DetailViewMixin(object):
    details_model = Blog
    context_detail_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super(DetailViewMixin, self).get_context_data(**kwargs)
        context[self.context_detail_object_name] = self.get_detail_object()
        context['comments'] = Comment.objects.all()
        return context

    def get_detail_object(self):
        return self.details_model._default_manager.get(pk=self.kwargs['pk'])

class BlogDetailView(DetailViewMixin, CreateView):

    model = Comment
    template_name = "detail.html"
    form_class = CommentForm

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('detail',kwargs = {'pk': pk})     

    def form_valid(self,form):
        form.instance.user = self.request.user
        form.instance.blog = Blog.objects.get(id = self.kwargs['pk'])

        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        post = Blog.objects.get(pk = pk)
        read_count = post.read_count
        read_count +=1
        post.read_count = read_count
        post.save()
        return super().get(request, *args, **kwargs)
        
class AddBlogView(CreateView):
    form_class = BlogForm
    model = Blog
    template_name = 'add-blog.html'
    success_url = '/'
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)
