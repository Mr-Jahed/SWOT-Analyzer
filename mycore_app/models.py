from django.db import models

# This model stores the SWOT analysis data entered by the user.
class SWOTEntry(models.Model):
    name = models.CharField(max_length=100)  # Person or project name
    strengths = models.TextField()           # List of strengths (min 2 required)
    weaknesses = models.TextField()          # List of weaknesses (min 2 required)
    opportunities = models.TextField()       # List of opportunities (min 2 required)
    threats = models.TextField()             # List of threats (min 2 required)
    submitted_at = models.DateTimeField(auto_now_add=True)  # Auto timestamp

    def __str__(self):
        return f"{self.name}'s SWOT"
