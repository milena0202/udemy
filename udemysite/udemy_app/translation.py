from .models import (User, Category, SubCategory, Course, Lesson,
                    Assignment)
from modeltranslation.translator import TranslationOptions, register

@register(User)
class UserTranslationOptions(TranslationOptions):
    fields = ('bio',)


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)


@register(SubCategory)
class SubCategoryTranslationOptions(TranslationOptions):
    fields = ('sub_category_name',)


@register(Course)
class CourseTranslationOptions(TranslationOptions):
    fields = ('description',)


@register(Lesson)
class LessonTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Assignment)
class AssignmentTranslationOptions(TranslationOptions):
    fields = ('title', 'description')





