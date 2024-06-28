
from django.views.generic import DetailView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from car.models import CarModel
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from user.forms import CommentForm
from django.contrib import messages
from django.shortcuts import redirect,render
from user.models import Purchase


class CarDetailView(DetailView):
    model=CarModel
    pk_url_kwarg='id'
    template_name='car_details.html'
    
    def post(self,request,*args,**kwargs):
        self.object=self.get_object()
        car=self.object
        
        if 'buy' in request.POST:
            if car.quantity>0:
                car.quantity-=1
                car.save()
                Purchase.objects.create(user=request.user,car=car)
                messages.success(request, f'You have successfully purchased {car.name}.')
            else:
                messages.error(request, f'Sorry, {car.name} is out of stock.')
            return redirect('car_details', id=car.pk)
        
        
        
        form=CommentForm(data=self.request.POST)
        if form.is_valid():
            new_comment=form.save(commit=False)
            new_comment.car=car
            new_comment.save()
        return self.get(request,*args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        car=self.object
        comments=car.comments.all()
        form=CommentForm()
        context['car']=car
        context['comments']=comments
        context['form']=form
        return context
    
@method_decorator(login_required,name='dispatch')
class PurchaseHistory(ListView):
    model = Purchase
    template_name = 'purchase_history.html'
    context_object_name = 'purchases'

    def get_queryset(self):
        return Purchase.objects.filter(user=self.request.user)

    
    