from django.contrib import admin
from django.urls import path
from startseite.views import startseite, register
from kalender.views import kalender
from django.contrib.auth import views as auth_views
from kalender.views import event_list_create
from notizen.views import note_list, create_note, edit_note, delete_note, note_detail
from kalender.views import event_update, event_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', startseite, name='startseite'),
    path('kalender/', kalender, name='kalender'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('api/events/', event_list_create, name='get-events'),
    path('notizen/<int:pk>/', note_detail, name='note_detail'),
    path('notizen/', note_list, name='note_list'),
    path('notizen/erstellen/', create_note, name='create_note'),
    path('notizen/<int:pk>/bearbeiten/', edit_note, name='edit_note'),
    path('notizen/<int:pk>/löschen/', delete_note, name='delete_note'),
    path('api/events/<int:pk>/', event_update, name='event_update'),
    path('api/events/<int:pk>/delete/', event_delete, name='event_delete'),

]
