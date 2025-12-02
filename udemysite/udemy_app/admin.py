from django.contrib import admin
from .models import  (User,  Category, SubCategory, Course, Lesson,
                     Assignment, Question, Option, Exam, Certificate,
                     Review)
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationInlineModelAdmin


class SubCategoryInline(admin.TabularInline, TranslationInlineModelAdmin):
    model = SubCategory
    extra = 1


class LessonInline(admin.TabularInline, TranslationInlineModelAdmin):
    model = Lesson
    extra = 1


class AssignmentInline(admin.TabularInline, TranslationInlineModelAdmin):
    model = Assignment
    extra = 1



@admin.register(Course)
class ProductAdmin(TranslationAdmin):
    inlines = [LessonInline, AssignmentInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Category)
class ProductAdmin(TranslationAdmin):
    inlines = [SubCategoryInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

admin.site.register(User)
admin.site.register(Exam)
admin.site.register(Option)
admin.site.register(Certificate)
admin.site.register(Review)
admin.site.register(Question)
