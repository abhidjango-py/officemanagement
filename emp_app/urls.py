from django.urls import path,include
from emp_app import views

urlpatterns = [
    path('',views.index,name='index'),
    path('view_emp',views.view_emp,name='view_emp'),
    path('add_emp',views.add_emp,name='add_emp'),
    path('rem_emp',views.rem_emp,name='rem_emp'),
    path('rem_emp/<int:emp_id>',views.rem_emp,name='rem_emp'),
    path('fil_emp',views.fil_emp,name='fil_emp'),
    ]