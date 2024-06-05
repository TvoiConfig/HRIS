from django.shortcuts import render
from bd.models import Staff
from .forms import StaffsForm
from django.views.generic import FormView
from django.urls import reverse_lazy
def index(request):
    return render(request, 'main/index.html')


def staff(request):
    staffs = Staff.objects.all()
    return render(request, 'main/Staff.html', {'staffs': staffs})


class StaffsView(FormView):
    template_name = 'orders.html'
    form_class = StaffsForm
    success_url = reverse_lazy("staff")

    def form_valid(self, form):
        if form.is_valid():
            print(self.request.FILES)
            form.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)