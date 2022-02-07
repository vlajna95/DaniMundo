from modeltranslation.translator import register, TranslationOptions
from .models import Article, CustomUser


@register(Article)
class ArticleTranslationOptions(TranslationOptions):
	fields = ["title", "summary", "body"]


@register(CustomUser)
class CustomUserTranslationOptions(TranslationOptions):
	fields = ["first_name", "last_name"]
