from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import (UserViewSet, CategoryListAPIView, CategoryDetailAPIView,
                    SubCategoryListAPIView, SubCategoryDetailAPIView,
                    CourseListAPIView, CourseDetailAPIView, LessonViewSet, AssignmentListAPIView,
                    AssignmentDetailAPIView, QuestionListAPIView, QuestionDetailAPIView,
                    OptionListAPIView, OptionDetailAPIView, ExamListAPIVew, ExamDetailAPIView,
                    CertificateListAPIView, CertificateDetailAPIView,
                    RegisterView, CustomLoginView, LogoutView, ReviewEditAPIView, ReviewCreateView,
                    CourseCreateAPIView, CourseEditAPIView)

router = SimpleRouter()
router.register('users', UserViewSet)
router.register('lesson', LessonViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view(), name='category-detail'),
    path('subcategories/', SubCategoryListAPIView.as_view(), name='subcategory-list'),
    path('subcategories/<int:pk>/', SubCategoryDetailAPIView.as_view(),name='subcategory-detail'),
    path('courses/', CourseListAPIView.as_view(), name='course-list'),
    path('courses/<int:pk>/', CourseDetailAPIView.as_view(), name='course-detail'),
    path('assignments/', AssignmentListAPIView.as_view(), name='assignment-list'),
    path('assignments/<int:pk>/', AssignmentDetailAPIView.as_view(), name='assignment-detail'),
    path('questions/', QuestionListAPIView.as_view(), name='question-list'),
    path('questions/<int:pk>/', QuestionDetailAPIView.as_view(), name='question-detail'),
    path('options/', OptionListAPIView.as_view(), name='option-list'),
    path('options/<int:pk>/', OptionDetailAPIView.as_view(), name='option-detail'),
    path('exams/', ExamListAPIVew.as_view(), name='exam-list'),
    path('exam/<int:pk>/', ExamDetailAPIView.as_view(), name='exam-detail'),
    path('certificates/', CertificateListAPIView.as_view(), name='certificate-list'),
    path('certificates/<int:pk>/', CertificateDetailAPIView.as_view(), name='certificate-detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('courses/create/', CourseCreateAPIView.as_view(), name='course-create'),
    path('courses/create/<int:pk>/', CourseEditAPIView.as_view(), name='course-detaill'),
    path('reviews/create/', ReviewCreateView.as_view(), name='review-create'),
    path('reviews/<int:pk>/', ReviewEditAPIView.as_view(), name='review-detail'),
]