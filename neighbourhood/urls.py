from neighbourhood import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',views.welcome,name = 'welcome'),
    path('about',views.about, name = 'about'),
    path('contacts',views.contacts, name = 'contacts'),
    path('signup', views.signup, name='signup'),
    path('login', LoginView.as_view(), name='login_url'),
    path('logout/', LogoutView.as_view(next_page='login_url'), name='logout_url'),
    path('post',views.post,name='post'),
    path('edit_profile/(?P<username>\w{0,50})',views.edit_profile, name='edit_profile'),
    path('search/', views.search_business, name='search'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)