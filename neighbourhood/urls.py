from django.urls import re_path as url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path


urlpatterns=[
    path('',views.index,name = 'index'),
    path('contacts',views.contacts, name = 'contacts'),
    path('signup', views.signup, name='signup'),
    path('login', LoginView.as_view(), name='login_url'),
    path('user/', views.profile, name='profile'),
    path('user/edit_profile/', views.edit_profile, name='edit_profile'),
    path('logout/', LogoutView.as_view(next_page='login_url'), name='logout_url'),
    path('post',views.add_post,name='post'),
    path('search/', views.search_business, name='search'),
    path('business',views.business,name = 'business'),
    path('accounts/profile/', views.profile, name='profile'),
    # path('edit_profile/',views.edit_profile, name='edit_profile'),
    # url(r'^api/business/$', views.BusinessList.as_view()),
    # url(r'^edit_profile/(?P<username>\w{0,50})',views.edit_profile, name='edit_profile'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
