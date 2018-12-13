from django.shortcuts import render

def post_list(request):
    return render(request, 'mainblog/post_list.html', {})
