from neighbourhood import views
from django.urls import path


urlpatterns=[
    path('',views.welcome,name = 'welcome'),
    path(r'^about$',views.about, name = 'about'),
    path(r'^contacts$',views.contacts, name = 'contacts'),
    path(r'^signup', views.signup, name='signup'),
    path(r'^login', LoginView.as_view(), name='login_url'),
    path(r'^logout/', LogoutView.as_view(next_page='login_url'), name='logout_url'),
    path(r'^post',views.post,name='post'),
    path(r'^edit_profile/(?P<username>\w{0,50})',views.edit_profile, name='edit_profile'),
    path(r'^search/', views.search_business, name='search'),
]
