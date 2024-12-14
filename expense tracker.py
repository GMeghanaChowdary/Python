from django.shortcuts import render
from .models import Expense
def expense_tracker(request):
    if request.method == "POST":
        name = request.POST["name"]
        amount = request.POST["amount"]
        Expense.objects.create(name=name, amount=amount)
    expenses = Expense.objects.all()
    return render(request, "expense_tracker.html", {"expenses": expenses})
