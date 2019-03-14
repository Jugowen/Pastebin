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
    path('post/set-watch/', WatchCreateView, name='post-setwatch'),
    path('post/watch', PostListView.as_view(template_name='post/watch_words.html'), name='post-watch'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='register/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='register/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='register/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='register/password_reset_complete.html'), name='password_reset_complete'),
]
