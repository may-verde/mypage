from django.contrib import admin
from django.urls import path
import myapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myapp.views.main, name="main"),
    path('blog/<int:post_id>', myapp.views.detail, name="detail"),
    path('blog/write/', myapp.views.write, name="write"),
    path('blog/create', myapp.views.create, name="create"),

]


