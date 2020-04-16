from django.urls import path

import views

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('blog', views.blog),
    path('contact', views.contact),
    path('portfolio', views.portfolio),
    path('github', views.github_api),
]

# Boilerplate to include static files
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

