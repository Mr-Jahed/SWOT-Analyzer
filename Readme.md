# My Personal SWOT Analyzer (Web App)

This is a simple Django web application that allows users to enter their personal or project-based SWOT analysis and view it in a formatted 2x2 matrix layout.

##  (Additionally) I have Deployed this Project Using Nggrok Allowed Host in Settings.py and Deployed Successfully..!
    - (Note: Ngrok is used for local development and testing purposes, not for production deployment...!)

---
##  Technologies Used
- Python 3.x
- Django (Backend Framework)
- HTML + CSS (Frontend)
- SQLite (Default Django database)(Not used because this project does not require as per manager demand )
- Bootstrap (Optional for styling)(same)

---

## 2.  How to Run the Project

Follow these steps to set up and run the project locally:

- To Create a Virtual Environment and Install Dependencies
- python -m venv env
# Windows
- env\Scripts\activate
# macOS/Linux
- source env/bin/activate

- pip install -r requirements.txt

- python manage.py makemigrations
- python manage.py migrate 


- python manage.py runserver(For Running the Server(Project))


## 3. Logic Behind the App-:

- Users enter their SWOT points into a simple form with at least 2 inputs per category.The submitted data is then rendered into a 2x2 matrix format     ( Strengths, Weaknesses, Opportunities, Threats), kind of like a digital self-reflection tool.

- Django form validation ensures user enters enough points before saving.

- Upon submission, the backend stores the entry in the database.

- A form where user types at least 2 points in each SWOT category.

  On clicking "Analyze", it shows a neatly formatted SWOT Matrix on the same page.

  Optionally shows a smart suggestion like:
  "Use your strength in public speaking to tackle the threat of team communication failure."

- The app also displays a basic suggestion using the first strength and threat input (e.g., “Use strength X to tackle threat Y”).

# (Imp)- At least 2 points in each SWOT category must fill, otherwise it will raise an Error That requires Must be Two or more Points

---

## 4. How It Works

# Frontend Form (HTML + CSS):
- The user sees a clean form with 4 textboxes — one for each SWOT category. They can write anything — maybe their coding skills, weaknesses, goals, or challenges.

## Submit Button:
- When the user clicks submit on Analyze, we send that form data to the Django backend using a POST request.

## Backend Logic (views.py):
- Django catches the data, checks each category (Strength, Weakness, etc.), and saves each one to the database as a SWOT model object.
  It saves both:
  What type it is (swot_type)
  What the user wrote (description)

## Database (models.py):
  Each entry is stored like:
  - Strength → “I’m good at Python”
  - Weakness → “I get nervous in meetings”
  - Opportunity → “I can learn Django”
  - Threat → “My team struggles with communication”

## Render Output:
- After saving, we redirect back and show all SWOT entries below the form. It’s like your personal SWOT board being built live.

## Small Things That Matter:
- CSRF token is used to protect the form submission (since Django requires it).

- I used @csrf_exempt just for quick testing with ngrok, but ideally we’d use the token properly.

- The design is simple but neat — no JavaScript yet, just pure Django and HTML/CSS.


##  No login or user system is required for this mini-project, but it can be added later.

