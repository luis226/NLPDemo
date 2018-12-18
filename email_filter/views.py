from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .machine_learning import SpamModel


# Create your views here.
class Index(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request,self.template_name)

    def post(self, request):
        msg = request.POST['email-content']
        ml_model = SpamModel()
        prediction = ml_model.predict(msg)
        not_spam, spam = prediction[0], prediction[1]
        context = {'spam': spam, "not_spam": not_spam, 'message': msg}
        return render(request, self.template_name, context=context)
