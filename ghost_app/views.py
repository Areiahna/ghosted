from django.shortcuts import render, HttpResponseRedirect, reverse
from django.utils import timezone
from ghost_app.models import PostModel
from ghost_app.forms import AddPostForm
# Create your views here.


def index_view(request):
    posts = PostModel.objects.order_by('-post_date')
    return render(request, "index.html", {"post": posts})


def create_post(request):
    if request.method == "POST":
        form = AddPostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            PostModel.objects.create(
                text=data.get("text"),
                post=data.get("post"),
            )
            return HttpResponseRedirect(reverse("homepage"))
    form = AddPostForm()
    return render(request, "post.html", {"form": form, "post": PostModel})


def upvote_view(request, post_id):
    post = PostModel.objects.filter(id=post_id).first()
    votes = post.upvotes
    post.upvotes = votes + 1
    return render(request, "vote.html", {"value": post.upvotes})
    return HttpResponseRedirect(reverse("homepage"))


def downvote_view(request, post_id):
    post = PostModel.objects.filter(id=post_id).first()
    votes = post.upvotes
    post.upvotes = votes - 1
    return render(request, "vote.html", {"value": post.upvotes})
    # return HttpResponseRedirect(reverse("homepage"))


def roast_post(request):
    post = PostModel.objects.filter(post="Roast").order_by('-post_date')
    return render(request, "roast.html", {"post": post})


def boast_post(request):
    post = PostModel.objects.filter(post="Boast").order_by('-post_date')
    return render(request, "boast.html", {"post": post})


def sorted_post(request):
    posts = PostModel.objects.order_by('-post_date')
    sorted_post = posts.order_by('-upvotes')

    # new_post = posts.order_by("post_time")
    return render(request, "sorted.html", {"post": sorted_post})
