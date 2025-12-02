from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    user_name = models.CharField(max_length=100)
    phone_number = PhoneNumberField()
    RoleChoices = (
        ('клиент', 'клиент'),
        ('преподаватель', 'преподаватель')
    )
    role = models.CharField(max_length=100, choices=RoleChoices, default='клиент')
    profile_picture = models.ImageField(upload_to='profile_picture/')
    bio = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.username

class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.category_name

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.sub_category_name

class Course(models.Model):
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='sub_categorys')
    course_name = models.CharField(max_length=100)
    description = models.TextField()
    LevelChoices = (
        ('начальный','начальный'),
        ('средний', 'средний'),
        ('продвинутый', 'продвинутый'),
    )
    price = models.PositiveIntegerField(default=1)
    level = models.CharField(max_length=100, choices=LevelChoices, )
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    course_image = models.ImageField(upload_to='course_image/', null=True, blank=True)

    def __str__(self):
        return self.course_name

    def get_avg_rating(self):
        rating = self.reviews.all()
        if rating.exists():
            return round(sum([i.rating for i in rating]) / rating.count(), 1)
        return 0

    def get_count_people(self):
        ratings = self.reviews.all()
        if ratings.exists():
            if ratings.count() > 200:
                return f'200+'
            elif ratings.count():
                return ratings.count()
        return 0


class Lesson(models.Model):
    title = models.CharField(max_length=100)
    video = models.URLField()
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')

    def __str__(self):
        return self.title

class Assignment(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Option(models.Model):
    option_name = models.CharField(max_length=100)
    type_option = models.BooleanField(null=True)

    def __str__(self):
        return self.option_name


class Question(models.Model):
    question_text = models.CharField(max_length=100)
    question_name = models.CharField(max_length=100, null=True, blank=True)
    option = models.ForeignKey(Option, on_delete=models.CASCADE, null=True, blank=True, related_name='options')

    def __str__(self):
        return self.question_name

class Exam(models.Model):
    title = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='exams_questions')
    duration = models.DurationField()

    def __str__(self):
        return self.title

class Certificate(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    issued_at = models.DateTimeField(auto_now_add=True)
    certificate_url = models.FileField (upload_to='certificates/'
                                    )

class Review(models.Model):
    user_review = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(choices=[(i, str(1))for i in (1, 6)])
    comment = models.TextField()
