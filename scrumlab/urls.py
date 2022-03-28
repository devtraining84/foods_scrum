"""scrumlab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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


from jedzonko.views import (
    IndexView,
    DashboardView,
    Recipe_list,
    get_recipt_details,
    add_plan
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view()),
    path('main/', DashboardView.as_view()),
    path('recipe/list', Recipe_list.as_view()),
    path('recipe/add', Recipe_list.as_view()),
    path('receipe/<int:id>', Recipe_list.as_view(), name="rec_list"),
    path('recipe/<int:id>/',get_recipt_details, name='recipt_det'),
    path('plan/add/',add_plan, name='plan_to_add'),

]

