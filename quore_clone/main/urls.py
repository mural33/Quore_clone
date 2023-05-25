from django.urls import path
from .import views

urlpatterns = [
    path("signin/",views.sign_in,name="sign_in"),
    path("login/",views.log_in,name="log_in"),
    path("email_check/",views.email_check,name="email_check"),
    path("home/",views.main,name="home"),
    path("post_problem/",views.problem_post,name="postproblem"),
    path("logout/",views.log_out,name="logout"),
    path("question_view/<slug:slug>",views.view,name="view")
]
