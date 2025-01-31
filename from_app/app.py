from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        resume_data = {
            "name": request.form.get("name"),
            "email": request.form.get("email"),
            "phone": request.form.get("phone"),
            "job_role": request.form.get("job_role"),
            "skills": request.form.get("skills"),
            "experience": request.form.get("experience"),
        }

        print("Received Resume Data:", resume_data)  # Debugging print
        return "Form submitted successfully!"
    
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
