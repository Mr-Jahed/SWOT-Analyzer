from django.shortcuts import render, redirect
from .forms import SWOTForm
from .models import SWOTEntry

# Main view that handles both the form and displaying the matrix after submission
def swot_view(request):
    form = SWOTForm()  # Empty form for GET request
    latest_entry = None
    suggestion = ""  # This will show a custom suggestion based on inputs

    if request.method == "POST":
        form = SWOTForm(request.POST)
        if form.is_valid():
            latest_entry = form.save()  # Save valid form data to DB
            form = SWOTForm()  # Reset form after submission

            # Generate a suggestion based on first strength and threat
            strengths = latest_entry.strengths.strip().split('\n')
            threats = latest_entry.threats.strip().split('\n')
            if strengths and threats:
                suggestion = f"Tip: Use your strength '{strengths[0]}' to overcome threat '{threats[0]}'."

    return render(request, 'swot_form.html', {
        'form': form,
        'entry': latest_entry,
        'suggestion': suggestion
    })
