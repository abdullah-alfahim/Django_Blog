from django.contrib import admin
from django.urls import path, include
from config.views import HomeView, BlogCreateView, ProfileView, DeleteView, UpdateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('blog/', BlogCreateView.as_view(), name='create'),  
    path("accounts/", include('accounts.urls')),  
    path('accounts/', include('django.contrib.auth.urls')), 
    path('profile/', ProfileView.as_view(), name='profile'),
    path('delete/<int:pk>/', DeleteView.as_view(), name='delete'),
    path('update/<int:pk>/', UpdateView.as_view(), name='update'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)