"""
Django management command для заполнения базы данных реалистичными данными
Использование: python manage.py shell < populate_database.py
или создайте management/commands/populate_db.py
"""

import os
import django
from datetime import datetime, timedelta
from django.utils import timezone
import random


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'udemysite.settings')
django.setup()

from django.contrib.auth import get_user_model
from udemy_app.models import (
    Category, SubCategory, Course, Lesson,
    Assignment, Option, Question, Exam, Certificate, Review
)

User = get_user_model()


def clear_database():
    """Очистка базы данных перед заполнением"""
    print("Очистка базы данных...")
    Review.objects.all().delete()
    Certificate.objects.all().delete()
    Exam.objects.all().delete()
    Question.objects.all().delete()
    Option.objects.all().delete()
    Assignment.objects.all().delete()
    Lesson.objects.all().delete()
    Course.objects.all().delete()
    SubCategory.objects.all().delete()
    Category.objects.all().delete()
    User.objects.filter(is_superuser=False).delete()
    print("База данных очищена.")


def create_users():
    """Создание пользователей"""
    print("Создание пользователей...")

    users_data = [
        # Преподаватели
        {
            'username': 'john_smith',
            'email': 'john.smith@example.com',
            'user_name': 'John Smith',
            'phone_number': '+996555123456',
            'role': 'преподаватель',
            'bio': 'Experienced programming instructor with 10+ years of experience',
            'bio_ru': 'Опытный преподаватель программирования с 10+ летним стажем',
            'password': 'password123'
        },
        {
            'username': 'maria_ivanova',
            'email': 'maria.ivanova@example.com',
            'user_name': 'Maria Ivanova',
            'phone_number': '+996555234567',
            'role': 'преподаватель',
            'bio': 'Web design and UX/UI specialist',
            'bio_ru': 'Специалист по веб-дизайну и UX/UI',
            'password': 'password123'
        },
        {
            'username': 'alex_petrov',
            'email': 'alex.petrov@example.com',
            'user_name': 'Alex Petrov',
            'phone_number': '+996555345678',
            'role': 'преподаватель',
            'bio': 'Data science and machine learning expert',
            'bio_ru': 'Эксперт по data science и машинному обучению',
            'password': 'password123'
        },
        {
            'username': 'elena_kozlova',
            'email': 'elena.kozlova@example.com',
            'user_name': 'Elena Kozlova',
            'phone_number': '+996555456789',
            'role': 'преподаватель',
            'bio': 'Foreign language instructor',
            'bio_ru': 'Преподаватель иностранных языков',
            'password': 'password123'
        },
        # Клиенты
        {
            'username': 'student1',
            'email': 'student1@example.com',
            'user_name': 'Aidar Bekov',
            'phone_number': '+996555567890',
            'role': 'клиент',
            'bio': 'Aspiring developer',
            'bio_ru': 'Начинающий разработчик',
            'password': 'password123'
        },
        {
            'username': 'student2',
            'email': 'student2@example.com',
            'user_name': 'Asel Toktoeva',
            'phone_number': '+996555678901',
            'role': 'клиент',
            'bio': 'Learning design',
            'bio_ru': 'Изучаю дизайн',
            'password': 'password123'
        },
    ]

    users = []
    for data in users_data:
        password = data.pop('password')
        bio_ru = data.pop('bio_ru', '')
        user = User.objects.create_user(**data)
        user.set_password(password)
        user.bio_ru = bio_ru
        user.save()
        users.append(user)

    print(f"Создано {len(users)} пользователей.")
    return users


def create_categories():
    """Создание категорий и подкатегорий"""
    print("Создание категорий...")

    categories_data = {
        'Programming': {
            'name_ru': 'Программирование',
            'subcategories': [
                ('Web Development', 'Веб-разработка'),
                ('Mobile Development', 'Мобильная разработка'),
                ('Data Science', 'Data Science'),
                ('Game Development', 'Игровая разработка'),
            ]
        },
        'Business': {
            'name_ru': 'Бизнес',
            'subcategories': [
                ('Entrepreneurship', 'Предпринимательство'),
                ('Management', 'Менеджмент'),
                ('Marketing', 'Маркетинг'),
                ('Finance', 'Финансы'),
            ]
        },
        'Design': {
            'name_ru': 'Дизайн',
            'subcategories': [
                ('Graphic Design', 'Графический дизайн'),
                ('UX/UI Design', 'UX/UI дизайн'),
                ('3D and Animation', '3D и анимация'),
                ('Web Design', 'Веб-дизайн'),
            ]
        },
        'Languages': {
            'name_ru': 'Языки',
            'subcategories': [
                ('English Language', 'Английский язык'),
                ('Russian Language', 'Русский язык'),
                ('Chinese Language', 'Китайский язык'),
            ]
        },
    }

    categories = {}
    for cat_name_en, cat_data in categories_data.items():
        category = Category.objects.create(
            category_name=cat_name_en,
            category_name_ru=cat_data['name_ru']
        )
        categories[cat_name_en] = {'object': category, 'subcategories': {}}

        for subcat_en, subcat_ru in cat_data['subcategories']:
            subcategory = SubCategory.objects.create(
                category=category,
                sub_category_name=subcat_en,
                sub_category_name_ru=subcat_ru
            )
            categories[cat_name_en]['subcategories'][subcat_en] = subcategory

    print(f"Создано {len(categories)} категорий.")
    return categories


def create_courses(categories, teachers):
    """Создание курсов"""
    print("Создание курсов...")

    courses_data = [
        {
            'category': 'Programming',
            'subcategory': 'Web Development',
            'course_name': 'Complete Python Django Course',
            'course_name_ru': 'Полный курс Python Django',
            'description': 'Learn Django from basics to advanced level. Build real web applications from scratch.',
            'description_ru': 'Изучите Django от основ до продвинутого уровня. Создайте реальные веб-приложения с нуля.',
            'level': 'начальный',
            'price': 5000,
        },
        {
            'category': 'Programming',
            'subcategory': 'Web Development',
            'course_name': 'React JS - Complete Guide',
            'course_name_ru': 'React JS - Полное руководство',
            'description': 'Master React JS and build modern interactive web applications.',
            'description_ru': 'Освойте React JS и создавайте современные интерактивные веб-приложения.',
            'level': 'средний',
            'price': 6000,
        },
        {
            'category': 'Programming',
            'subcategory': 'Data Science',
            'course_name': 'Machine Learning A-Z',
            'course_name_ru': 'Машинное обучение от А до Я',
            'description': 'Complete machine learning course with Python. Learn algorithms and build models.',
            'description_ru': 'Полный курс по машинному обучению с Python. Изучите алгоритмы и создавайте модели.',
            'level': 'продвинутый',
            'price': 8000,
        },
        {
            'category': 'Design',
            'subcategory': 'UX/UI Design',
            'course_name': 'UX/UI Design for Beginners',
            'course_name_ru': 'UX/UI дизайн для начинающих',
            'description': 'Learn to create beautiful and functional interfaces.',
            'description_ru': 'Научитесь создавать красивые и функциональные интерфейсы.',
            'level': 'начальный',
            'price': 4500,
        },
        {
            'category': 'Design',
            'subcategory': 'Graphic Design',
            'course_name': 'Adobe Photoshop Masterclass',
            'course_name_ru': 'Adobe Photoshop - Мастер-класс',
            'description': 'From beginner to professional in Adobe Photoshop.',
            'description_ru': 'От новичка до профессионала в Adobe Photoshop.',
            'level': 'средний',
            'price': 5500,
        },
        {
            'category': 'Business',
            'subcategory': 'Marketing',
            'course_name': 'Digital Marketing 2024',
            'course_name_ru': 'Цифровой маркетинг 2024',
            'description': 'Modern digital marketing and promotion strategies.',
            'description_ru': 'Современные стратегии цифрового маркетинга и продвижения.',
            'level': 'начальный',
            'price': 7000,
        },
        {
            'category': 'Languages',
            'subcategory': 'English Language',
            'course_name': 'English for IT Professionals',
            'course_name_ru': 'Английский для IT специалистов',
            'description': 'Technical English for working in international IT companies.',
            'description_ru': 'Технический английский для работы в международных IT компаниях.',
            'level': 'средний',
            'price': 4000,
        },
        {
            'category': 'Programming',
            'subcategory': 'Mobile Development',
            'course_name': 'Flutter - Mobile App Development',
            'course_name_ru': 'Flutter - Разработка мобильных приложений',
            'description': 'Build cross-platform mobile apps with Flutter.',
            'description_ru': 'Создавайте кроссплатформенные мобильные приложения с Flutter.',
            'level': 'средний',
            'price': 6500,
        },
    ]

    courses = []
    for i, data in enumerate(courses_data):
        cat_name = data.pop('category')
        subcat_name = data.pop('subcategory')
        description_ru = data.pop('description_ru')
        course_name_ru = data.pop('course_name_ru', '')

        subcategory = categories[cat_name]['subcategories'][subcat_name]
        teacher = teachers[i % len(teachers)]

        course = Course.objects.create(
            sub_category=subcategory,
            created_by=teacher,
            **data
        )
        course.description_ru = description_ru
        if course_name_ru:
            course.course_name_ru = course_name_ru
        course.save()
        courses.append(course)

    print(f"Создано {len(courses)} курсов.")
    return courses


def create_lessons(courses):
    """Создание уроков"""
    print("Создание уроков...")

    lessons_templates = [
        {
            'title': 'Introduction to the Course',
            'title_ru': 'Введение в курс',
            'content': 'Welcome! In this lesson we will get familiar with the course program.',
            'content_ru': 'Добро пожаловать! В этом уроке мы познакомимся с программой курса.',
            'video': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
        },
        {
            'title': 'Basic Concepts',
            'title_ru': 'Основные концепции',
            'content': 'Learning fundamental concepts and principles.',
            'content_ru': 'Изучаем фундаментальные концепции и принципы.',
            'video': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
        },
        {
            'title': 'Practical Session',
            'title_ru': 'Практическое занятие',
            'content': 'Applying acquired knowledge in practice.',
            'content_ru': 'Применяем полученные знания на практике.',
            'video': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
        },
        {
            'title': 'Advanced Techniques',
            'title_ru': 'Продвинутые техники',
            'content': 'Learning advanced methods and approaches.',
            'content_ru': 'Изучаем продвинутые методы и подходы.',
            'video': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
        },
        {
            'title': 'Final Project',
            'title_ru': 'Финальный проект',
            'content': 'Creating the final course project.',
            'content_ru': 'Создаем итоговый проект курса.',
            'video': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
        },
    ]

    lessons = []
    for course in courses:
        for i, template in enumerate(lessons_templates):
            title_ru = template['title_ru']
            content_ru = template['content_ru']

            lesson = Lesson.objects.create(
                course=course,
                title=template['title'],
                content=template['content'],
                video=template['video']
            )
            lesson.title_ru = title_ru
            lesson.content_ru = content_ru
            lesson.save()
            lessons.append(lesson)

    print(f"Создано {len(lessons)} уроков.")
    return lessons


def create_assignments(courses, students):
    """Создание заданий"""
    print("Создание заданий...")

    assignments_data = [
        {
            'title': 'Practical Assignment 1',
            'title_ru': 'Практическое задание 1',
            'description': 'Complete exercises from the first course module.',
            'description_ru': 'Выполните упражнения из первого модуля курса.',
        },
        {
            'title': 'Intermediate Project',
            'title_ru': 'Промежуточный проект',
            'description': 'Create a mini-project using learned material.',
            'description_ru': 'Создайте мини-проект используя изученный материал.',
        },
    ]

    assignments = []
    for course in courses[:3]:  # Только для первых 3 курсов
        for student in students:
            for template in assignments_data:
                title_ru = template['title_ru']
                description_ru = template['description_ru']

                assignment = Assignment.objects.create(
                    course=course,
                    student=student,
                    title=template['title'],
                    description=template['description'],
                    due_date=timezone.now().date() + timedelta(days=random.randint(7, 30))
                )
                assignment.title_ru = title_ru
                assignment.description_ru = description_ru
                assignment.save()
                assignments.append(assignment)

    print(f"Создано {len(assignments)} заданий.")
    return assignments


def create_questions_and_exams(courses):
    """Создание вопросов и экзаменов"""
    print("Создание вопросов и экзаменов...")

    # Создание вариантов ответов
    options_data = [
        ('Вариант A', 'Option A', True),
        ('Вариант B', 'Option B', False),
        ('Вариант C', 'Option C', False),
        ('Вариант D', 'Option D', False),
    ]

    options = []
    for option_ru, option_en, is_correct in options_data:
        option = Option.objects.create(
            option_name=option_ru,
            type_option=is_correct
        )
        options.append(option)

    # Создание вопросов
    questions = []
    for i in range(10):
        question = Question.objects.create(
            question_text=f'Вопрос {i + 1}: Выберите правильный ответ',
            question_name=f'Вопрос {i + 1}',
            option=random.choice(options)
        )
        questions.append(question)

    # Создание экзаменов
    exams = []
    for course in courses:
        exam = Exam.objects.create(
            title=f'Итоговый экзамен - {course.course_name}',
            course=course,
            question=random.choice(questions),
            duration=timedelta(hours=2)
        )
        exams.append(exam)

    print(f"Создано {len(questions)} вопросов и {len(exams)} экзаменов.")
    return questions, exams


def create_reviews(courses, students):
    """Создание отзывов"""
    print("Создание отзывов...")

    comments = [
        'Отличный курс! Очень доволен результатом.',
        'Хороший материал, но хотелось бы больше практики.',
        'Преподаватель объясняет очень понятно.',
        'Курс превзошел мои ожидания!',
        'Рекомендую всем начинающим.',
        'Качественный контент и отличная подача материала.',
    ]

    reviews = []
    for course in courses:
        # Создаем от 5 до 15 отзывов на курс
        num_reviews = random.randint(5, 15)
        for _ in range(num_reviews):
            student = random.choice(students)
            rating = random.randint(3, 5)  # Рейтинг от 3 до 5

            review = Review.objects.create(
                user_review=student,
                course=course,
                rating=rating,
                comment=random.choice(comments)
            )
            reviews.append(review)

    print(f"Создано {len(reviews)} отзывов.")
    return reviews


def populate_database():
    """Главная функция для заполнения базы данных"""
    print("=" * 50)
    print("ЗАПОЛНЕНИЕ БАЗЫ ДАННЫХ")
    print("=" * 50)

    # Очистка базы (раскомментируйте если нужно)
    # clear_database()

    # Создание данных
    users = create_users()
    teachers = [u for u in users if u.role == 'преподаватель']
    students = [u for u in users if u.role == 'клиент']

    categories = create_categories()
    courses = create_courses(categories, teachers)
    lessons = create_lessons(courses)
    assignments = create_assignments(courses, students)
    questions, exams = create_questions_and_exams(courses)
    reviews = create_reviews(courses, students)

    print("=" * 50)
    print("ЗАВЕРШЕНО!")
    print(f"Пользователей: {len(users)}")
    print(f"Категорий: {len(categories)}")
    print(f"Курсов: {len(courses)}")
    print(f"Уроков: {len(lessons)}")
    print(f"Заданий: {len(assignments)}")
    print(f"Вопросов: {len(questions)}")
    print(f"Экзаменов: {len(exams)}")
    print(f"Отзывов: {len(reviews)}")
    print("=" * 50)


if __name__ == '__main__':
    populate_database()