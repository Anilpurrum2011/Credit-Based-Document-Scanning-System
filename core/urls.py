<<<<<<< HEAD
from django.urls import path, include
from .views import home, register, upload_document, list_documents, extract_text
from authentication.views import login_view, logout_view  # Import authentication views if they are in authentication app

urlpatterns = [
    path('', home, name="home"),  # Home page
    path("auth/", include("authentication.urls")),  # Ensure correct app name
    path('register/', register, name='register'),  # Registration page
    path('login/', login_view, name='login'),  # Login page
    path('logout/', logout_view, name='logout'),  # Logout view
    path("auth/", include("authentication.urls")),  # Include authentication URLs from authentication app
    path('upload/', upload_document, name="upload_document"),  # File upload
    path('list/', list_documents, name="list_documents"),  # List uploaded documents
    path('extract/<int:document_id>/', extract_text, name="extract_text"),  # Extract text from document
]

=======
from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name="home"),
]
>>>>>>> fc540e5 (Initial commit - Django setup for CrediScan)
