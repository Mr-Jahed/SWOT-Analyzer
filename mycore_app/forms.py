from django import forms
from .models import SWOTEntry

# This form will be used to collect user inputs for all 4 SWOT fields
# and validate that there are at least 2 points in each.
class SWOTForm(forms.ModelForm):
    class Meta:
        model = SWOTEntry
        fields = '__all__'  # Include all fields from the SWOTEntry model

        # Customize the input fields with larger text areas
        widgets = {
            'strengths': forms.Textarea(attrs={'rows': 3}),
            'weaknesses': forms.Textarea(attrs={'rows': 3}),
            'opportunities': forms.Textarea(attrs={'rows': 3}),
            'threats': forms.Textarea(attrs={'rows': 3}),
        }

    # Custom validation to make sure each field has at least 2 bullet points
    def clean(self):
        cleaned_data = super().clean()

        # Helper function to count lines (ignores empty lines)
        def count_points(text):
            return len([line for line in text.strip().split('\n') if line.strip() != ""])

        if count_points(cleaned_data.get('strengths', '')) < 2:
            self.add_error('strengths', "Please enter at least 2 strengths.")
        if count_points(cleaned_data.get('weaknesses', '')) < 2:
            self.add_error('weaknesses', "Please enter at least 2 weaknesses.")
        if count_points(cleaned_data.get('opportunities', '')) < 2:
            self.add_error('opportunities', "Please enter at least 2 opportunities.")
        if count_points(cleaned_data.get('threats', '')) < 2:
            self.add_error('threats', "Please enter at least 2 threats.")
