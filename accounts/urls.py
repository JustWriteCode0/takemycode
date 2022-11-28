from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views 
from .views import user_registration, user_login, user_logout, user_profiles

urlpatterns = [
    path('registration', user_registration, name='registration'),
    path('login/', user_login, name='login'),
    path('logout', user_logout, name='logout'),
    path('<user_name>', user_profiles, name="users_profiles"),

    path('reset_password/', views.PasswordResetView.as_view(template_name="accounts/html/reset_password.html"), name="reset_password"),
    path('reset_password_sent/', views.PasswordResetDoneView.as_view(template_name="accounts/html/reset_password_done.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(template_name="accounts/html/reset_password_complete.html"), name="password_reset_confirm"),
    path('reset_password_complete/', views.PasswordResetCompleteView.as_view(template_name="accounts/html/reset_password_done.html"), name="password_reset_complete"),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    