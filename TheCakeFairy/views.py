from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect,get_object_or_404
from .forms import Usersform
from django.contrib import messages
from services.models import Contact
from services.models import Payment
from services.models import Product


def aboutUS(request):
    return render(request,"about.html")

def homepage(request):
    context={}
    if request.method=="POST":
        name=request.POST.get("name")
        em=request.POST.get("email")
        num=request.POST.get("contactno")
        sub=request.POST.get("query")
        msz=request.POST.get("message")

        obj= Contact(name=name, email=em, number=num,subject=sub,message=msz)
        obj.save()
        context['message']=f"Dear {name}, Thank you for visiting The Cake Fairy ! "
    return render(request,"index.html",context)

def shop(request):
    return render(request,"shop.html")

def review(request):
    return render(request,"review.html")

def blogs(request):
    return render(request,"blogs.html")

def product(request):
    return render(request,"product.html")

def product7(request):
    return render(request,"product-7.html")

def product1(request):
    return render(request,"product-1.html")

def product2(request):
    return render(request,"product-2.html")

def product3(request):
    return render(request,"product-3.html")

def product4(request):
    return render(request,"product-4.html")

def product5(request):
    return render(request,"product-5.html")

def product6(request):
    return render(request,"product-6.html")

def product8(request):
    return render(request,"product-8.html")

def payment(request):
    context={}
    if request.method=="POST":
        id=request.POST.get("product_name_id")
        card_number=request.POST.get("card_number")
        card_holder_name=request.POST.get("card_holder")
        date=request.POST.get("expiration_date")
        cvv=request.POST.get("cvv")
        # msz=request.POST.get("message")

        obj= Payment(product_name_id=id, card_number=card_number, card_holder=card_holder_name, expiration_date=date, cvv=cvv)
        obj.save()
        # Add a success message
        messages.success(request, "Payment Successful. Thank you for visiting The Cake Fairy!")
        context['message']=f"Payment for {id} is Successful , Thank you for visiting The Cake Fairy ! "
        return redirect("index.html")  # Assuming "index" is the name of your index page URL patternank you for visiting The Cake Fairy ! "
    return render(request,"payment.html",context)
    

def contact(request):
    context={}
    if request.method=="POST":
        name=request.POST.get("name")
        em=request.POST.get("email")
        num=request.POST.get("contactno")
        sub=request.POST.get("query")
        msz=request.POST.get("message")

        obj= Contact(name=name, email=em, number=num,subject=sub,message=msz)
        obj.save()
        context['message']=f"Dear {name}, Thank you for visiting The Cake Fairy ! "
    return render(request,"contact.html",context)

# def login(request):
#     return render(request,"login.html")

def userform(request):
    finalans=0
    fn=Usersform()
    data={'form':fn}
    try:
        if request.method=="POST":
        # n1=request.GET['num1']
        # n2=request.GET['num2']
            n1=int(request.POST.get('num1'))
            n2=int(request.POST.get('num2'))
            finalans=n1+n2
            data={
                'n1':n1,
                'n2':n2,
                'output':finalans,
                'form':fn
            }
            url="/contact/?output={}".format(finalans)
            #return HttpResponseRedirect('/about/')
            return redirect(url)
    except:
        pass

    return render(request,"userform.html",data)

def submitform(request):
    try:
        if request.method=="POST":
        # n1=request.GET['num1']
        # n2=request.GET['num2']
            n1=int(request.POST.get('num1'))
            n2=int(request.POST.get('num2'))
            finalans=n1+n2
            data={
                'n1':n1,
                'n2':n2,
                'output':finalans
            }
            return HttpResponse(finalans)
            #return HttpResponseRedirect('/about/')
            #return redirect(url)
    except:
        pass


def payment_details(request):
    context={}
    if request.method=="POST":
        card_number=request.POST.get("card_number")
        card_holder_name=request.POST.get("card_holder")
        date=request.POST.get("expiration_date")
        cvv=request.POST.get("cvv")
        # msz=request.POST.get("message")

        obj= Contact(card_number=card_number, card_holder=card_holder_name, expiration_date=date, cvv=cvv)
        obj.save()
        context['message']=f"Payment Successful , Thank you for visiting The Cake Fairy ! "
    return render(request,"index.html",context)
    


