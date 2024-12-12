"""
URL configuration for webpage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path
from .views import templatehome
# from  app_one.views import display_one
# from  app_two.views import display_two



# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path("",home,name="index"),
#     path("contact",subscribe,name="thankyou")
# ]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path("",home,name="index"),
#     path("contact",subscribe,name="thankyou"),
#     path("one/",display_one,name="index1"),
#     path("two/",display_two,name="index2"),
# ]


urlpatterns = [
    path('admin/', admin.site.urls),
    # path("",home,name="index"),
    path("",templatehome,name="templatehome"),
   
]