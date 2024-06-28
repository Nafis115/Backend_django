from django.shortcuts import render,redirect
from . import forms
from . import models
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from django.utils.decorators import method_decorator
# Create your views here.
def add_post(request):
    if request.method=="POST":
        postForm=forms.PostForm(request.POST)
        if postForm.is_valid():
            postForm.instance.author=request.user
            postForm.save()
            return redirect("add_post")
    else:
        postForm=forms.PostForm()
    return render(request,"add_post.html",{'form':postForm})

@method_decorator(login_required,name='dispatch')
class AddPostCreateView(CreateView):
    model=models.Post
    form_class=forms.PostForm
    template_name = 'add_post.html'
    success_url= reverse_lazy('add_post')
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)


def edit_post(request,id):
    post=models.Post.objects.get(pk=id)
    post_form=forms.PostForm(instance=post)
    if request.method=="POST":
        post_form=forms.PostForm(request.POST,instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect("homepage")
    return render(request,'add_post.html', {'form': post_form})

@method_decorator(login_required,name='dispatch')
class UpdatePost(UpdateView):
    model=models.Post
    form_class=forms.PostForm
    template_name='add_post.html'
    success_url=reverse_lazy('profile')
    pk_url_kwarg='id'

@method_decorator(login_required,name='dispatch')
class DeletePost(DeleteView):
    model=models.Post
    template_name='Delete.html'
    success_url=reverse_lazy('profile')
    pk_url_kwarg='id'
    
def delete_post(request,id):
    post=models.Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')

@method_decorator(login_required,name='dispatch')
class DetailsView(DetailView):
    model=models.Post
    pk_url_kwarg='id'
    template_name='post_detail.html'
    
    def post(self,request,*args,**kwargs):
        self.object = self.get_object()
        form=forms.CommentForm(data=self.request.POST)
        post=self.object
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request,*args,**kwargs)
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post=self.object
        comments=post.comments.all()
        form=forms.CommentForm()
        context["comments"] =comments 
        context["form"] =form
        return context
    
   
    
            