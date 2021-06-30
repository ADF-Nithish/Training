import datetime
from django.test import TestCase,Client
from django.urls import reverse
from FirstAPP.models import Request_Info,Response_Info
from FirstAPP.forms import RequestInfoForm
# Create your tests here.

class TestModels(TestCase):
    def setUp(self):
        self.client = Client()
        self.req = Request_Info.objects.create(
            city="Covai",
            date_of_birth=datetime.date(2000,1,18),
            first_name="TestCase",last_name="T",
            gender="Male",nationality="India",state="Assam",pincode=641004,
            qualification="B.TECH",pan_number="BR400",salary=40000)
        Request_Info.objects.create(
            city="Covai",
            date_of_birth=datetime.date(2000,1,18),
            first_name="TestCase2",last_name="T",
            gender="Male",nationality="India",state="Tamil Nadu",pincode=641004,
            qualification="B.TECH",pan_number="ERERE",salary=40000,)
        self.res = Response_Info.objects.create(response="success",request_id=self.req)

    def test_model(self):
        self.assertEqual(len(Request_Info.objects.all()),2)
        self.assertEqual(Response_Info.objects.get(request_id=self.req).response,"success")

    def test_form_request(self):
        form = RequestInfoForm(
            data={
                'city':"Covai",
                'date_of_birth': datetime.date(2000,1,18),
                'first_name': "TestCase",
                'last_name': "T",
                'gender': "Male",
                'nationality': "India",
                'state': "Assam",
                'pincode': 641004,
                'qualification': "B.TECH",
                'pan_number': "TEST50PAN",
                'salary': 40000
            }
        )
        self.assertTrue(form.is_valid())
    def test_not_valid_state(self):
        form = RequestInfoForm(
            data={
                'city':"Covai",
                'date_of_birth': datetime.date(2000,1,18),
                'first_name': "TestCase",
                'last_name': "T",
                'gender': "Male",
                'nationality': "India",
                'state': "TamilNadu",
                'pincode': 641004,
                'qualification': "B.TECH",
                'pan_number': "TEST50PAN",
                'salary': 40000
            }
        )
        self.assertFalse(form.is_valid())
    def test_not_valid_nationality(self):
        form = RequestInfoForm(
            data={
                'city':"Covai",
                'date_of_birth': datetime.date(2000,1,18),
                'first_name': "TestCase",
                'last_name': "T",
                'gender': "Male",
                'nationality': "Africa",
                'state': "TamilNadu",
                'pincode': 641004,
                'qualification': "B.TECH",
                'pan_number': "TEST50PAN",
                'salary': 40000
            }
        )
        self.assertFalse(form.is_valid())
    def test_not_valid_not_user_repeated(self):
        form = RequestInfoForm(
            data={
                'city':"Covai",
                'date_of_birth': datetime.date(2000,1,18),
                'first_name': "TestCase",
                'last_name': "T",
                'gender': "Male",
                'nationality': "India",
                'state': "Tamil Nadu",
                'pincode': 641004,
                'qualification': "B.TECH",
                'pan_number': "ERERE",
                'salary': 40000
            }
        )
        self.assertTrue(form.is_valid())
    def test_not_valid_salary(self):
        form = RequestInfoForm(
            data={
                'city':"Covai",
                'date_of_birth': datetime.date(2000,1,18),
                'first_name': "TestCase",
                'last_name': "T",
                'gender': "Male",
                'nationality': "India",
                'state': "Tamil Nadu",
                'pincode': 641004,
                'qualification': "B.TECH",
                'pan_number': "NEWPAN",
                'salary': 5000
            }
        )
        self.assertFalse(form.is_valid())
    def test_not_valid_age_calculate(self):
        form = RequestInfoForm(
            data={
                'city':"Covai",
                'date_of_birth': datetime.date(2001,1,18),
                'first_name': "TestCase",
                'last_name': "T",
                'gender': "Male",
                'nationality': "India",
                'state': "TamilNadu",
                'pincode': 641004,
                'qualification': "B.TECH",
                'pan_number': "TEST50PAN",
                'salary': 400000
            }
        )
        self.assertFalse(form.is_valid())
    def test_no_form(self):
        form = RequestInfoForm(data={})
        self.assertFalse(form.is_valid())
    def test_not_valid_user_repeated(self):
        Request_Info.objects.create(
            city="Covai",
            date_of_birth=datetime.date(2000,1,18),
            first_name="TestCase2",last_name="T",
            gender="Male",nationality="India",state="Tamil Nadu",pincode=641004,
            qualification="B.TECH",pan_number="VVVVV",salary=40000,)
        form = RequestInfoForm(
            data={
                'city':"Covai",
                'date_of_birth': datetime.date(2000,1,18),
                'first_name': "TestCase",
                'last_name': "T",
                'gender': "Male",
                'nationality': "India",
                'state': "Tamil Nadu",
                'pincode': 641004,
                'qualification': "B.TECH",
                'pan_number': "VVVVV",
                'salary': 40000
            }
        )
        self.assertFalse(form.is_valid())
    def test_views_get(self):
        response = self.client.get(reverse('RequestForm'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'index.html')
    def test_view_post(self):
        url = reverse('RequestForm')
        form = RequestInfoForm(
            data={
                'city':"Covai",
                'date_of_birth': datetime.date(2000,1,18),
                'first_name': "TestCase",
                'last_name': "T",
                'gender': "Male",
                'nationality': "India",
                'state': "Assam",
                'pincode': 641004,
                'qualification': "B.TECH",
                'pan_number': "MMMMM",
                'salary': 40000
            }
        )
        response = self.client.post(url,form.data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'index.html')
    def test_view_post_errors(self):
        url = reverse('RequestForm')
        form = RequestInfoForm(
            data={
                'city':"Covai",
                'date_of_birth': datetime.date(2001,1,18),
                'first_name': "TestCase",
                'last_name': "T",
                'gender': "Male",
                'nationality': "India",
                'state': "TamilNadu",
                'pincode': 641004,
                'qualification': "B.TECH",
                'pan_number': "ERERE",
                'salary': 4000
            }
        )
        response = self.client.post(url,form.data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'failed.html')