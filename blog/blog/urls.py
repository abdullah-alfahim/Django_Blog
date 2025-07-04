# project/urls.py
from django.contrib import admin
from django.urls import path, include # Make sure 'include' is imported
from config.views import HomeView, BlogCreateView # Assuming config.views is where HomeView is
from django.conf import settings
from django.conf.urls.static import static
# from django.contrib.auth import views as auth_views # No longer explicitly needed here if using include('django.contrib.auth.urls')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('blog/', BlogCreateView.as_view(), name='create'),  # Assuming you want to create a blog post
    # Include the URLs for your custom accounts app
    path("accounts/", include('accounts.urls')),  # Your custom accounts app URLs
    path('accounts/', include('django.contrib.auth.urls')), # Django's built-in auth URLs (includes 'login', 'logout', 'password_change', etc.)
    # REMOVE THIS LINE: path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
]

# BOTH static AND media files in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Removed trailing comma here, it was creating a tuple