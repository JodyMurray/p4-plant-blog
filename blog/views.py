from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.views.generic import FormView
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from .models import Post, Profile, User
from django.contrib import messages
from .forms import CommentForm, EditProfileForm


class UserProfile(generic.ListView):
    model = Profile
    queryset = Profile.objects.all()
    template_name = 'profile.html'


class UserSettings(View):

    def dispatch(self, request, *args, **kwargs):
        self.profile, __ = Profile.objects.get_or_create(user=request.user)
        return super(UserSettings, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        context = {'profile': self.profile}
        return render(request, 'edit_profile.html', context)

    def post(self, request):
        form = EditProfileForm(
            request.POST, request.FILES, instance=self.profile)

        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()

            messages.success(request, 'Profile saved')
        else:
            messages.error(
                request,
                'Profile could not be updated.'
            )
        return redirect('profile')


class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = [
        'title',
        'author',
        'content',
        'excerpt',
        'featured_image',
        'status']


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3


class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,

            "post.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class PostLike(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class FeaturedView(generic.TemplateView):

    model = Post
    template_name = "feature.html"


def FeaturedPost(request):
    template_name = "featured_post.html"

    return render(request, 'featured_post.html')


def PetsPost(request):
    template_name = "pets.html"

    return render(request, "pets.html")


def delete_post(request, id):
    # success_message = ("Your Post has been deleted")
    post = Post.objects.filter(id=id)
    post.delete()
    messages.success(
            request,
            'Post deleted successfully.'
        )

    # messages.success(self.request, self.success_message)
    return redirect('/')


def edit_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]

        post.title = title
        post.content = content
        post.save()
        return redirect(f"/edit/{post.id}", redirect('home'))
    return render(request, "update_post.html", {"post": post})

