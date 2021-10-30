from django.urls import path
from . import views


urlpatterns = [
	path('register/', views.registerPage, name="register"),
 
    path("login/", views.login_request, name="login"),
    path('accept/',views.accept,name='accept'),
    path('ccpage/',views.ccpage,name='ccpage'),
    path('addevent/',views.add_event,name='addevent'),
    path('viewclub/',views.club,name='club'),
    path('view_events/<str:pk>/',views.view_events,name='view_events'),
  
 
    
    path('stu_view_events/<str:pk>/',views.stu_view_events,name='stu_view_events'),
    path('stu_clubs/',views.student_club,name='student_club'),
    path('student/',views.student,name='student'),
    path('registration/',views.registration_form,name='registration_form'),
    path('participants/<str:pk>/',views.reg_part,name='reg_part'),
    path('/',views.logoutUser,name='logout'),
    path('',views.faq,name='faq')

  


]