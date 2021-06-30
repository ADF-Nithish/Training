import datetime
from django.test import TestCase
from FirstAPP.models import Request_Info,Response_Info
# Create your tests here.

class Request_Info_TestCase(TestCase):
    def setUp(self):
        Request_Info.objects.create(city="Covai",
        date_of_birth=datetime.date(2000,1,18),first_name="TestCase",last_name="T",
        gender="Male",nationality="India",state="Assam",pincode=641004
        ,qualification="B.TECH",pan_number="BR400",salary=40000)

    def get(self):
        assert isinstance(Request_Info.objects.get(pan_number = "BR400"),Request_Info)

