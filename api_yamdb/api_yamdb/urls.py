from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

apipatterns = [
    path('', include('user.urls')),
    path('', include('reviews.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(apipatterns)),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc',
    ),
]
