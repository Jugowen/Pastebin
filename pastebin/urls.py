from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from post.views import home, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, WatchCreateView
from register.views import register, profile
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', PostListView.as_view(), name='posts'),
    path('', PostListView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='register/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='register/logout.html'), name='logout'),
    path('profile/', profile, name='profile'),
    path('post/private', PostListView.as_view(template_name='post/private.html'), name='post-private'),
    path('post/invited', PostListView.as_view(template_name='post/invited.html'), name='post-invite'),
    path('post/watch/', WatchCreateView.as_view(), name='post-watch'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
