from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from core.services.category_service import CategoryService
from core.services.item_service import ItemService
from .data import (
    user,
    ratings,
    user_messages,
)

cat_service = CategoryService()
item_service = ItemService()
folder_path = "../templates/user"


ctx = {
    "ratings": ratings,
    "items": item_service.get_all_items(),
    "user_messages": user_messages,
}


@login_required
def home(request):
    ctx["user"] = request.user
    return render(request, f"{folder_path}/index.html", context=ctx)


@login_required
def edit(request):
    ctx["user"] = request.user
    return render(request, f"{folder_path}/edit.html", context=ctx)


@login_required
def profile(request, id):
    ctx["user"] = request.user
    return render(request, f"{folder_path}/user.html", context=ctx)


@login_required
def history(request):
    ctx["user"] = request.user
    ctx["active_sales"] = item_service.get_sale_items(request.user)
    ctx["sold_items"] = item_service.get_sale_items(request.user, is_sold=True)
    return render(request, f"{folder_path}/history.html", context=ctx)


@login_required
def messages(request):
    ctx["user"] = request.user
    return render(request, f"{folder_path}/messages.html", context=ctx)
