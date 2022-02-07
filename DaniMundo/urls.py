from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
	path("grappelli/", include("grappelli.urls")),
	path("lang/", include("django.conf.urls.i18n")),
]

urlpatterns += i18n_patterns(
	path("admin/", admin.site.urls),
	path("blog/", include("blog.urls")),
	path("", TemplateView.as_view(template_name="home.html"), name="home"),
	prefix_default_language=False
)
