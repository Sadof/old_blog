from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm,addPostForm
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import permission_required
from django.db.models import Q

#def index(request):
    #latest_post_list = Post.objects.order_by('-pub_date')[:5]
    #context = {'latest_post_list' : latest_post_list}
    #return render(request, 'blog/index.html',context)
class IndexView(generic.ListView):
    template_name = "blog/index.html"
    context_object_name = 'latest_post_list'
    #paginate_by = 2
    def get_queryset(self):
        return Post.objects.order_by("-pub_date").filter(pub_date__lte=timezone.now())



class searchList(generic.ListView):
    template_name = "blog/index.html"
    context_object_name = 'latest_post_list'
    model = Post
    def get_queryset(self):
        query = self.request.GET.get("search","")
        object_list = Post.objects.filter(Q(post_author__username__contains=query) | Q(post_title__contains=query))
        return object_list

class DetailView(generic.DetailView):
    model = Comment
    template_name = 'blog/detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['post'] =  Post.objects.get(pk=self.kwargs['pk'])
        context['form'] = CommentForm()
        num_visits = self.request.session.get('num_visits', 0)
        self.request.session['num_visits'] = num_visits + 1
        context['visits'] = self.request.session['num_visits']
        return context
    ''' def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                new_comment = form.save(commit=False)
                print(new_comment)
                new_comment.post = post.id
                new_comment.user = form.cleaned_data["user"]
                new_comment.topic = form.cleaned_data["text"]
                print(timezone.now())
                new_comment.date = timezone.now()
                form.save()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            form = CommentForm()
        return render(request, 'blog/detail.html', {'post': post, 'form': form})'''
    def get_queryset(self):
        return Post.objects.filter(pub_date__lte=timezone.now())


class addPostView(CreateView):
    template_name = "blog/add_post.html"
    form_class = addPostForm
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.post_author = self.request.user
        self.object.save()
        return HttpResponseRedirect("/blog/")

def add_comment(request, post_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = Post.objects.get(pk=post_id)
            new_comment.user = request.user
            new_comment.topic = form.cleaned_data["text"]
            new_comment.date = timezone.now()
            form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponseRedirect(reverse('blog:post', args=(post_id,)))

@permission_required('blog.delete_post')
def delete_post(request, post_id):
    object = Post.objects.get(pk=post_id)
    object.delete()
    return HttpResponseRedirect("/blog/")
#def comment(request, post_id):


