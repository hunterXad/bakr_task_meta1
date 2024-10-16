
# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from .models import Reservation
from .forms import ReservationForm
from django.contrib.auth.decorators import login_required

@login_required
def list_reservations(request):
    reservations = Reservation.objects.filter(customer=request.user)
    return render(request, 'reservations/reservation_list.html', {'reservations': reservations})

@login_required
def create_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.customer = request.user
            reservation.save()
            return redirect('reservation_list')
    else:
        form = ReservationForm()
    return render(request, 'reservations/reservation_forms.html', {'form': form})

@login_required
def update_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk, customer=request.user)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('reservation_list')
    else:
        form = ReservationForm(instance=reservation)
    return render(request, 'reservations/reservation_forms.html', {'form': form})

@login_required
def delete_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk, customer=request.user)
    if request.method == 'POST':
        reservation.delete()
        return redirect('reservation_list')
    return render(request, 'reservations/reservation_confirm_delete.html', {'reservation': reservation})

def template(request):
    recent_reservations = Reservation.objects.order_by('-date')[:5]
    
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ReservationForm()

    context = {
        'recent_reservations': recent_reservations,
        'form': form
    }
    
    return render(request, 'template.html', context)


