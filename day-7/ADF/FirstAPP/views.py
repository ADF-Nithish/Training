from django.shortcuts import render
from django.views import generic
from FirstAPP.forms import RequestInfoForm
from FirstAPP.models import Request_Info,Response_Info
# Create your views here.


class FormView(generic.View):
    template_name = 'index.html'

    def get(self, request):
        form = RequestInfoForm()
        r = Request_Info.objects.all()
        context = {'form': form.as_p(), 'r': r}
        return render(request, self.template_name, context=context)

    def post(self, request):
        form = RequestInfoForm(request.POST)
        context = {'form': form.as_p()}
        if form.is_valid():
            form.save()
            curr_id = Request_Info.objects.all().filter(
                pan_number=form.cleaned_data.get('pan_number')).order_by('id').last().id
            response_message = "success"
            curr_req = Request_Info.objects.get(id=curr_id)
            Response_Info.objects.create(request_id=curr_req,response=response_message)
        else:
            response_message = form.non_field_errors().as_data()[0]
            Response_Info.objects.create(response=
            str(response_message).strip('[]').strip('\'\''))
        return render(request, self.template_name, context=context)
    
