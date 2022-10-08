from django.test import TestCase, Client
from django.urls import reverse
from django.db.models import Max
from courses.models import Course, Info
from courses.views import course
from .models import Student
from django.contrib.auth.models import User
# Create your tests here.

class CourseViewTestCase(TestCase):

    def setUp(self):

        #create course name
        course1 = Course.objects.create(code="AAA", name="subject A")
        course2 = Course.objects.create(code="BBB", name="subject B")

        #create info about course
        Info.objects.create(subname = course1, semester = '1', year = '1111', seat = '1', status = 'available')
        Info.objects.create(subname = course2, semester = '2', year = '2222', seat = '22', status = 'available')

        #create student name
        student1 = Student.objects.create(first="AAAA", last="BBBB")
        student2 = Student.objects.create(first="CCCC", last="DDDD")
        student1.subject.add(course2)
        student2.subject.add(course1)
        student2.subject.add(course2)
        #create user
        self.user = User.objects.create_user('test_user', password='test_user')
        c = Client()
        c.login(username='test_user', password='test_user')

    def test_index_view_status_code(self):
        """ index view's status code is ok """
        c = Client()
        c.login(username='test_user', password='test_user')
        response = c.get(reverse('users:index'))
        self.assertEqual(response.status_code, 200)

    def test_index_wrong(self):
        """ wrong username or password """
        c = Client()
        c.login(username='wrong_user', password='wrong_user')
        response = c.get(reverse('users:index'))
        self.assertEqual(response.status_code, 302)

    def test_login_view_status_code(self):
        """ login view's status code is ok """

        c = Client()
        response = c.get(reverse('users:login'))
        self.assertEqual(response.status_code, 200)


    def test_regist_view_status_code(self):
        """ regist view's status code is ok """

        c = Client()
        response = c.get(reverse('users:regist'))
        self.assertEqual(response.status_code, 200)

    def test_regist_view_context(self):
        """ context is correctly set """

        c = Client()
        response = c.get(reverse('users:regist'))
        self.assertEqual(response.context['courses'].count(), 2)

    def test_remove_view_status_code(self):
        """ remove view's status code is ok """

        c = Client()
        response = c.get(reverse('users:remove'))
        self.assertEqual(response.status_code, 200)

    def test_remove_view_context(self):
        """ context is correctly set """

        c = Client()
        response = c.get(reverse('users:remove'))
        self.assertEqual(response.context['courses'].count(), 2)

    
    def test_status_result_page(self):
        """  result page should return status code 200 """

        c = Client()
        f = Student.objects.first()
        response = c.get(reverse('users:result', args=(f.id+1,)))
        self.assertEqual(response.status_code, 200)


    def test_valid_result_view_context(self):
        """ context is correctly set """

        c = Client()
        f = Student.objects.first()  #student1 have 1 subject
        response = c.get(reverse('users:result', args=(f.id+1,)))
        self.assertEqual(
            response.context['sublist'].count(), 1)

    
    def test_book_view(self):
        """ check if seat decrease"""
        
        f = Info.objects.first()
        c = Client()
        c.post(reverse('users:book',args=(f.id+1,)), {'subject':f.id})
        f2 = Info.objects.first()
        self.assertEqual(f2.seat, 0)
    
    def test_delete_view(self):
        """ check if seat increase """

        l = Info.objects.last()
        c = Client()
        c.post(reverse('users:delete',args=(l.id+1,)), {'remove':l.id})
        l2 = Info.objects.last()
        self.assertEqual(l2.seat, 23)

    def test_book_view_2(self):
        """ check if status change"""
        
        f = Info.objects.first()
        c = Client()
        c.post(reverse('users:book',args=(f.id+1,)), {'subject':f.id})
        f2 = Info.objects.first()
        self.assertEqual(f2.status, 'unavailable')
    
    def test_delete_view_2(self):
        """ status should not change """

        l = Info.objects.last()
        c = Client()
        c.post(reverse('users:delete',args=(l.id+1,)), {'remove':l.id})
        l2 = Info.objects.last()
        self.assertEqual(l2.status, 'available')