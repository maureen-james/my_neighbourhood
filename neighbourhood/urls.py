from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path


urlpatterns=[
    path('',views.welcome,name = 'welcome'),
    url(r'^contacts$',views.contacts, name = 'contacts'),
    # url(r'^signup', views.signup, name='signup'),
    url(r'^login', LoginView.as_view(), name='login_url'),
    url(r'^logout/', LogoutView.as_view(next_page='login_url'), name='logout_url'),
    url(r'^post',views.post,name='post'),
    url(r'^edit_profile/(?P<username>\w{0,50})',views.edit_profile, name='edit_profile'),
    url(r'^search/', views.search_business, name='search'),
    url(r'^business',views.business,name = 'business'),
    # url(r'^api/business/$', views.BusinessList.as_view()),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
