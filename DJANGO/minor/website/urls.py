
from django.urls import path
from . import views
from . import signup
from . import recommendation
from . import SecondRecommendation

urlpatterns = [
    path('',views.index,name="Home"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('order/',views.order,name="order"),
    path('signup/',signup.signup_user,name="signup"),
    path('login/',views.login_user,name="login"),
    path('logout/',views.logout_user,name="logout"),
    path('create_profile/',signup.create_profile,name="create_profile"),
    path('buy/',views.buy,name="buy"),
    path('decider/',views.decider,name="decider"),
    path('recommend/',recommendation.Recommend,name="recommend"),
    path('SecondRecommend/',SecondRecommendation.Recommend,name="SecondRecommend"),
    path('LikeRate/',views.LikeRate,name="LikeRate"),
]