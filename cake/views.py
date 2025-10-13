from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .models import Item1,About,special,Gallaryy,Category

def home(request):
    items =Item1.objects.all()
    item=About.objects.all()
    item2=special.objects.all()
   
    return render(request, "cake/index.html",{'items':items,
                                            'item':item, 
                                            })
def about(request):
    items =Item1.objects.all()
    item=About.objects.all()
    item2=special.objects.all()
    return render (request,"cake/about-us.html",{'items':items,
                                            'item':item })
def full(request):
    item=About.objects.all()
    items = Item1.objects.all()
    category = request.GET.get('category')

    categories = Category.objects.all()   # for filter menu

    if category is None or category == "all":
        item2 = Gallaryy.objects.all()
    else:
        item2 = Gallaryy.objects.filter(catagory__Cname=category)

    return render(
        request,
        "cake/portfolio-full-width.html",
        {
            'items': items,
            'item2': item2,
            'categories': categories,
             'item':item,# send to template
        }
    )



