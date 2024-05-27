from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', add_card, name='add_card'),
    path('card/', card_list, name='card_list'),
    path("addtocard/<int:pk>", addtocard, name='addtocard'),  # Updated this line
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
