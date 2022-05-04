from django.shortcuts import render, redirect
from .data import categories, user, categories_with_parents

folder_path = "../templates/user"


ctx = {
    "categories": categories,
    "user": user,
    "sub_categories": categories_with_parents,
}


def home(request):
    return render(request, f"{folder_path}/index.html", context=ctx)


def edit(request):
    if user is None:
        return redirect("/login")
    return render(request, f"{folder_path}/edit.html")


def profile(request, id):
    return render(request, f"{folder_path}/user.html", context=ctx)


def history(request):
    return render(request, f"{folder_path}/history.html", context=ctx)


def messages(request):
    return render(request, f"{folder_path}/messages.html", context=ctx)


def messages(request):
<<<<<<< HEAD
    return render(request, f"{folder_path}/messages.html")
=======
    return render(request, f"{folder_path}/messages.html", context=ctx)
>>>>>>> origin/main