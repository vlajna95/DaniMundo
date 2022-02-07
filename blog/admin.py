from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from django.utils.translation import ngettext_lazy
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Article


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
	model = CustomUser
	add_form = CustomUserCreationForm
	form = CustomUserChangeForm
	# prepopulated_fields = {"slug": ("username", )}
	list_display = ["first_name", "last_name", "username", "email", "view_articles_link", "date_joined", "last_login"]
	list_filter = ["date_joined", "last_login"]
	search_fields = ["first_name", "last_name", "username", "email"]

	def view_articles_link(self, obj):
		count = obj.articles.count()
		url = (reverse("admin:blog_article_changelist") + "?" + urlencode({"author__id": f"{obj.id}"}))
		link_text = ngettext_lazy("%(count)d article", "%(count)d articles", count) % {"count": count}
		return format_html("<a href=\"{}\">" + link_text + "</a>", url)
	view_articles_link.short_description = _("Articles")


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title", )}
	list_display = ["title", "summary", "status", "view_authors_link", "date_created", "date_updated"]
	list_filter = ["author", "status", "date_created", "date_updated"]
	search_fields = ["title", "summary", "body"]

	def view_authors_link(self, obj):
		count = obj.author.count()
		url = (reverse("admin:blog_customuser_changelist") + "?" + urlencode({"articles__id": f"{obj.id}"}))
		link_text = ngettext_lazy("%(count)d author", "%(count)d authors", count) % {"count": count}
		return format_html("<a href=\"{}\">" + link_text + "</a>", url)
	view_authors_link.short_description = _("Authors")
