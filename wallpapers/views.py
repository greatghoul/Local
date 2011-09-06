from django.shortcuts import redirect
from django.shortcuts import render_to_response

from django.http import HttpResponse

def cate_list(request):
    """ List all wallpaper categories """
    return HttpResponse('categry list')

def cate_add(request):
    """ Add a category """
    return HttpResponse('add a category')

def cate_edit(request, cate_id):
    """ Edit a category """
    return HttpResponse('edit a category')

def cate_del(request, cate_id):
    """ Delete a category """
    return HttpResponse('delete a category')
