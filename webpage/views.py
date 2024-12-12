from django.shortcuts import render
# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("<b>This is my first webpage using django framework</b>")

# def subscribe(request):
#     return HttpResponse("Dont forget to subscribe....")


def templatehome(request):
    data ={'name':'swarnali'}
    return render(request,'welcome.html',data)