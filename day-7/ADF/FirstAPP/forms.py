import datetime
from django import forms
from FirstAPP.models import Request_Info

class RequestInfoForm(forms.ModelForm):
    class Meta:
        model = Request_Info
        fields = '__all__'
        years = [2001,2000,1999,1998,1997,1996]
        widgets = {
            'date_of_birth':forms.SelectDateWidget(years=years)
        }
    def clean(self):
        cleaned_data = super().clean()
        def age_calculate(birth_date,gender):
            today = datetime.date.today()
            age = today.year - birth_date.year - (
                (today.month, today.day) < (birth_date.month, birth_date.day))
            if (age >= 21 and  gender == 'Male') or (
                age >= 18 and gender == 'Female'):
                return True
            raise forms.ValidationError('Age is less than expected')
        def is_user_repeated(pan_number):
            r = Request_Info.objects.all().filter(pan_number = pan_number)
            if len(r) != 0 :
                r = r[len(r)-1]
            else:
                return True
            today = datetime.date.today()
            if ((today - r.request_received.date()).days) >= 5:
                return True
            raise forms.ValidationError('Recently request received in last 5 days.')
        def is_indian_or_american(nationality):
            if nationality.lower() == 'india' or nationality.lower() == 'america':
                return True
            raise forms.ValidationError('User should be from india or america')
        def check_state(state):
            states = ['andhra pradesh','arunachal pradesh',
            'assam','bihar','chhattisgarh','karnataka','madhya pradesh','odisha',
            'tamil nadu','telangana','west_bengal']
            if state.lower() in states:
                return True
            raise forms.ValidationError('Enter a valid State')
        def check_salary(salary):
            if salary > 10000 and salary < 90000:
                return True
            raise forms.ValidationError(
                'Salary should be greater than 10000 and less than 90000')
        
        age_calculate(cleaned_data.get('date_of_birth'),cleaned_data.get('gender'))
        is_user_repeated(cleaned_data.get('pan_number'))
        is_indian_or_american(cleaned_data.get('nationality'))
        check_state(cleaned_data.get('state'))
        check_salary(cleaned_data.get('salary'))
