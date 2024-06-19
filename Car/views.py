from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from Car import models
from .forms import CarForm, CommentForm
from django.contrib import messages
from django.views.generic import DetailView
from django.shortcuts import render, get_object_or_404
from .models import Car,Order

@login_required
def buy_car(request, pk):
    car = get_object_or_404(Car, pk=pk)
    
    if car.quantity > 0:
        car.quantity -= 1
        car.save()
        
        Order.objects.create(user=request.user, car=car, quantity=1)
        
        messages.success(request, f'You have successfully bought {car.name}!')
        return redirect('user_profile')
    else:
        messages.error(request, 'Sorry, this car is out of stock.')
        return redirect('car_details', pk=pk)

@login_required
def create_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Car added successfully')
            return redirect('home') 
    else:
        form = CarForm()
    
    return render(request, 'create_car.html', {'form': form})

class CarDetails(DetailView):
    model = models.Car
    template_name = 'car_details.html'
    
    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect('car_details', pk=post.pk)
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comments = post.comments.all()
        comment_form = CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
    

    
