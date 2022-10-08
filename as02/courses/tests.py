from django.test import TestCase, Client
from django.urls import reverse
from django.db.models import Max
from .models import Course, Info
# Create your tests here.

class CourseViewTestCase(TestCase):

    def setUp(self):

        #create course name
        courese1 = Course.objects.create(code="AAA", name="subject A")
        courese2 = Course.objects.create(code="BBB", name="subject B")

        #create info about course
        Info.objects.create(subname = courese1, semester = '1', year = '1111', seat = '11', status = 'aaa')
        Info.objects.create(subname = courese2, semester = '2', year = '2222', seat = '22', status = 'bbb')

    def test_index_view_status_code(self):
        """ index view's status code is ok """

        c = Client()
        response = c.get(reverse('courses:index'))
        self.assertEqual(response.status_code, 200)

    def test_index_view_context(self):
        """ context is correctly set """

        c = Client()
        response = c.get(reverse('courses:index'))
        self.assertEqual(
            response.context['courses'].count(), 2)
    
    def test_valid_course_page(self):
        """ valid course page should return status code 200 """

        c = Client()
        f = Course.objects.first()
        response = c.get(reverse('courses:course', args=(f.id,)))
        self.assertEqual(response.status_code, 200)

    def test_invalid_course_page(self):
        """ invalid course page should return status code 404 """

        max_id = Course.objects.all().aggregate(Max("id"))['id__max']

        c = Client()
        response = c.get(reverse('courses:course', args=(max_id+1,)))
        self.assertEqual(response.status_code, 404)

    