from django.shortcuts import render, get_object_or_404, redirect
from .models import Bill

# View for customers to see their bills
def customer_bill_list(request):
    if request.user.is_authenticated:
        bills = Bill.objects.filter(customer=request.user) 
        return render(request, 'bills/customer_bill_list.html', {'bills': bills})
    else:
        # Redirect to login or show an error message
        return redirect('bills:login')  # Change this to your login URL name

# View for marking a bill as paid
def mark_bill_paid(request, bill_id):
    bill = get_object_or_404(Bill, id=bill_id)
    if bill.payment_status == 'unpaid':
        bill.payment_status = 'paid'
        bill.save()
    return redirect('bills:customer_bill_list')

# View for admins to see all bills
def admin_bill_list(request):
    bills = Bill.objects.all()
    return render(request, 'bills/admin_bill_list.html', {'bills': bills})