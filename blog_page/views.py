from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Post, Quote
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .forms import PostForm, create_cat, QuoteForm
from django.urls import reverse_lazy
from django.templatetags.static import static
from django.contrib.auth.decorators import login_required




@login_required
def blog_post(request):
    blog_post = Post.objects.all().order_by('-date_posted')
    categories = Category.objects.all()
    quotes = Quote.objects.all()
    mood_images = {
        1: static('blog_page/images/crying.png'),
        2: static('blog_page/images/sad.png'),
        3: static('blog_page/images/neutral.png'),
        4: static('blog_page/images/smiling.png'),
        5: static('blog_page/images/lovely.png')
    }

    if request.method == 'POST':
        if request.POST['form_type'] == 'form1':
            post_form = PostForm(request.POST)
            if post_form.is_valid():
                post_form.save()
                return redirect('home')  # Redirect after form submission
            
        elif request.POST['form_type'] == 'form2':
            quote_form = QuoteForm(request.POST)
            if quote_form.is_valid():
                quote_form.save()
                return redirect('home')
        elif request.POST['form_type'] == 'delete':
            post_id = request.POST.get('post_id')
            print(post_id)
            post = get_object_or_404(Post, pk=post_id)
            post.delete()
            return redirect('home')




    else:
        post_form = PostForm()
        quote_form = QuoteForm()


    context = {
        'posts': blog_post,
        'categories': categories,
        'post_form': post_form,
        'mood_images': mood_images,
        'quotes': quotes,
        'quote_form': quote_form
    }

    return render(request, 'blog_page.html', context)



class EditPost(UpdateView):
    model = Post
    fields = ['content', 'mood', 'title']
    template_name = 'edit_post.html'
    success_url = reverse_lazy('home')

class CreateCategory(CreateView):
    model = Category
    form_class = create_cat
    success_message = 'New category created!'
    template_name = 'create_cat.html'
    success_url = reverse_lazy('home')

class DeletePost(DeleteView):
    model = Post
    template_name = 'deletepost.html'
    success_url = reverse_lazy('home')
