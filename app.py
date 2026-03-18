from flask import Flask, render_template, request

app = Flask(__name__)

questions = [
    {
        "id": "q1",
        "text": "What time do you feel most productive?",
        "options": ["Early morning", "Afternoon", "Evening", "Late night"]
    },
    {
        "id": "q2",
        "text": "How long can you study without losing focus?",
        "options": ["20-30 minutes", "45 minutes", "1 hour", "More than 1 hour"]
    },
    {
        "id": "q3",
        "text": "Which subject do you struggle with the most?",
        "options": ["Math", "Science", "Social Studies", "Languages"]
    },
    {
        "id": "q4",
        "text": "How do you prefer learning?",
        "options": ["Watching videos", "Reading notes", "Practicing questions", "Group discussion"]
    },
    {
        "id": "q5",
        "text": "What distracts you the most while studying?",
        "options": ["Phone", "Noise", "Overthinking", "Sleepiness"]
    },
    {
        "id": "q6",
        "text": "How often do you revise what you study?",
        "options": ["Daily", "Sometimes", "Before exams", "Rarely"]
    },
    {
        "id": "q7",
        "text": "What is your main goal?",
        "options": ["Score higher marks", "Understand concepts", "Finish syllabus", "Stay consistent"]
    },
    {
        "id": "q8",
        "text": "Where do you usually study best?",
        "options": ["Quiet room", "Library", "With music", "With friends"]
    },
    {
        "id": "q9",
        "text": "How do you feel before exams?",
        "options": ["Confident", "A little nervous", "Very stressed", "Unprepared"]
    },
    {
        "id": "q10",
        "text": "How many hours do you study daily right now?",
        "options": ["Less than 1 hour", "1-2 hours", "3-4 hours", "More than 4 hours"]
    }
]


def generate_suggestion(answers):
    study_time = "Evening"
    study_session = "45-minute focused sessions with 10-minute breaks"
    learning_style = "Practice-based learning"
    focus_area = "Consistency"
    revision = "Revise daily for 15-20 minutes"
    motivation = "Set small goals and reward yourself after each session"
    bonus = "Keep your phone away while studying"
    stress_tip = "Stay calm and trust your preparation."

    if "Early morning" in answers:
        study_time = "Early morning"
    elif "Late night" in answers:
        study_time = "Late night"
    elif "Afternoon" in answers:
        study_time = "Afternoon"

    if "20-30 minutes" in answers:
        study_session = "25-minute Pomodoro sessions with 5-minute breaks"
    elif "1 hour" in answers:
        study_session = "1-hour deep work sessions with 10-minute breaks"
    elif "More than 1 hour" in answers:
        study_session = "90-minute focused blocks with proper revision gaps"

    if "Watching videos" in answers:
        learning_style = "Video learning + short summary notes"
    elif "Reading notes" in answers:
        learning_style = "Structured note-based learning"
    elif "Practicing questions" in answers:
        learning_style = "Active recall and question practice"
    elif "Group discussion" in answers:
        learning_style = "Discussion-based collaborative study"

    if "Phone" in answers:
        focus_area = "Reducing mobile distraction"
        bonus = "Use focus mode or keep your phone in another room"
    elif "Noise" in answers:
        focus_area = "Creating a quiet study environment"
        bonus = "Use earplugs, soft instrumental music, or a quiet room"
    elif "Overthinking" in answers:
        focus_area = "Building mental clarity and confidence"
        bonus = "Start with the easiest task to reduce stress and build momentum"
    elif "Sleepiness" in answers:
        focus_area = "Improving energy and alertness"
        bonus = "Study after washing your face, stretching, and sitting upright"

    if "Daily" in answers:
        revision = "You already revise well — continue with short daily reviews"
    elif "Before exams" in answers:
        revision = "Start spaced revision every 2-3 days instead of only before exams"
    elif "Rarely" in answers:
        revision = "Use a weekly revision timetable to remember topics longer"

    if "Score higher marks" in answers:
        motivation = "Solve previous year questions and focus on high-weight chapters"
    elif "Understand concepts" in answers:
        motivation = "Study slowly but deeply, and teach concepts to yourself aloud"
    elif "Finish syllabus" in answers:
        motivation = "Make a chapter checklist and track progress every day"
    elif "Stay consistent" in answers:
        motivation = "Build a routine with fixed study hours instead of long random sessions"

    if "Very stressed" in answers:
        stress_tip = "Use deep breathing, revise key topics first, and avoid panic studying."
    elif "Unprepared" in answers:
        stress_tip = "Start with important chapters, make a mini-plan, and focus on progress over perfection."

    if "Less than 1 hour" in answers:
        bonus += " Try increasing your daily study time little by little."
    elif "More than 4 hours" in answers:
        bonus += " Make sure you include breaks to avoid burnout."

    return {
        "study_time": study_time,
        "study_session": study_session,
        "learning_style": learning_style,
        "focus_area": focus_area,
        "revision": revision,
        "motivation": motivation,
        "bonus": bonus,
        "stress_tip": stress_tip
    }


@app.route("/", methods=["GET"])
def home():
    return render_templates("index.html", questions=questions)


@app.route("/result", methods=["POST"])
def result():
    username = request.form.get("username", "Student").strip()
    if not username:
        username = "Student"

    answers = []
    for question in questions:
        answer = request.form.get(question["id"])
        if answer:
            answers.append(answer)

    suggestion = generate_suggestion(answers)

    return render_templates(
        "result.html",
        username=username,
        suggestion=suggestion
    )


if __name__ == "__main__":
    app.run(debug=True)