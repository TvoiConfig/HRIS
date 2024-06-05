from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as userViews
from django.contrib.auth import views as authViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('registration/', userViews.register, name="reg"),
    path('login/', authViews.LoginView.as_view(template_name='users/auth.html'), name='user'),
    path('exit/', authViews.LogoutView.as_view(template_name='main/index.html'), name='exit'),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
