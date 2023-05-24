from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import basic_dtl_project_bee_farm_website.common_app.urls

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include(basic_dtl_project_bee_farm_website.common_app.urls))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
