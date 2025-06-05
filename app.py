import streamlit as st

# Title of the quiz
# st.title("Quiz. Welche Integrationsform passt zu Ihrem Unternehmen?")

# Questions and scoring logic
questions = [
    {
        "question": "Wie stark möchte ihr Unternehmen die bestehende Organisationsstruktur für Nachhaltigkeit verändern?",
        "options": [
            ("Nur minimale Anpassungen auf Projektebene", 1),
            ("Ergänzungen durch neue Initiativen, ohne die Grundstruktur anzutasten", 2),
            ("Einführung neuer Bewertungsmechanismen für Prioritäten", 3),
            ("Grundlegende Neuausrichtung der Wertströme und Organisation", 4),
        ],
    },
    {
        "question": "Wie reif ist ihr Unternehmen im Umgang mit agilen Methoden und Nachhaltigkeit?",
        "options": [
            ("Erste Erfahrungen mit agilen Projekten und Nachhaltigkeit", 1),
            ("Agilität ist etabliert, aber Nachhaltigkeit ist noch nicht tief integriert", 2),
            ("Nachhaltigkeit ist wichtig und wird zunehmend in Entscheidungsprozesse integriert", 3),
            ("Nachhaltigkeit ist integraler Bestandteil aller Geschäftsprozesse und Strukturen", 4),
        ],
    },
    {
        "question": "Wie viel Ressourcen und Koordination kann ihr Unternehmen für Nachhaltigkeitsinitiativen aufwenden?",
        "options": [
            ("Begrenzt, lieber einfache Ziele auf Projektebene", 1),
            ("Mittel, mit bereichsübergreifenden Epics machbar", 2),
            ("Hoch, mit Fokus auf systematische Steuerungsmechanismen", 3),
            ("Sehr hoch, für umfassende organisatorische Veränderungen", 4),
        ],
    },
    {
        "question": "Wie wichtig ist es für ihr Unternehmen, Nachhaltigkeit nicht nur als Pflicht, sondern als Wettbewerbsvorteil zu sehen?",
        "options": [
            ("Erste Schritte, Fokus liegt noch auf Compliance", 1),
            ("Nachhaltigkeit gewinnt an Bedeutung, es gibt erste strategische Initiativen", 2),
            ("Nachhaltigkeit ist fest in der strategischen Priorisierung verankert", 3),
            ("Nachhaltigkeit prägt alle zentralen Geschäftsprozesse und Entscheidungen", 4),
        ],
    },
    {
        "question": "Wie schnell möchte ihr Unternehmen erste Nachhaltigkeitserfolge sehen?",
        "options": [
            ("Kurzfristige Erfolge in einzelnen Projekten", 1),
            ("Schnelle Umsetzung durch fokussierte Epics möglich", 2),
            ("Priorisierung führt mittelfristig zu strukturellen Veränderungen", 3),
            ("Langfristige Transformation mit umfassendem Impact", 4),
        ],
    },
]

# Recommendations based on score
recommendations = [
    (range(5, 8), "Option 1 – Taktische Integration: Minimaler Eingriff auf Projektebene, ideal für Unternehmen mit begrenzten Ressourcen oder ersten Schritten im Nachhaltigkeitsmanagement."),
    (range(8, 12), "Option 2 – Operative Integration: Hybrides Setup mit Sustainability Epics, passend für Unternehmen, die Nachhaltigkeit stärker operationalisieren wollen, ohne die Organisation komplett umzustellen."),
    (range(12, 16), "Option 3 – Ökonomische Integration: Nachhaltigkeit wird durch ökonomische Steuerungsmechanismen priorisiert, geeignet für Unternehmen mit ausgeprägter strategischer Nachhaltigkeitsausrichtung."),
    (range(16, 21), "Option 4 – Systematische Integration: Nachhaltigkeit ist tief in der Organisationsstruktur verankert, ideal für Unternehmen, die eine umfassende Transformation anstreben und langfristige Wirkung erzielen wollen."),
]

# Session state to track progress and score
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
if "scores" not in st.session_state:
    st.session_state.scores = []

# Add a landing page with a "Jetzt starten" button
if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False

if not st.session_state.quiz_started:
    st.title("Quiz. Welche Integrationsform passt zu Ihrem Unternehmen?")
    if st.button("Jetzt starten"):
        st.session_state.quiz_started = True
        st.session_state.current_question = 0
        st.session_state.scores = []
else:
    # Prevent IndexError by ensuring current_question does not exceed the number of questions
    current_question = st.session_state.current_question
    if current_question < len(questions):
        question = questions[current_question]
        # Format the questions in bold using Markdown
        st.markdown(f"**{question['question']}**")

        # Save the selected option in session state and pre-select it when navigating back
        if f"selected_option_{current_question}" not in st.session_state:
            st.session_state[f"selected_option_{current_question}"] = None

        selected_option = st.radio(
            "Bitte wählen Sie eine Option:",
            [opt[0] for opt in question["options"]],
            index=[opt[0] for opt in question["options"]].index(st.session_state[f"selected_option_{current_question}"]) if st.session_state[f"selected_option_{current_question}"] else None,
            key=f"question_{current_question}",
            label_visibility="hidden"
        )

        # Navigation buttons
        col1, col2 = st.columns(2)
        # Ensure the "Zurück" button is not displayed on the first question
        if current_question > 0 and col1.button("Zurück"):
            st.session_state.current_question -= 1
            st.session_state.scores.pop()

        # Ensure the "Weiter" button properly transitions to the results page
        if col2.button("Weiter"):
            if not selected_option:
                st.warning("Bitte wählen Sie eine Antwort aus")
            else:
                st.session_state[f"selected_option_{current_question}"] = selected_option
                score = next((opt[1] for opt in question["options"] if opt[0] == selected_option), None)
                if len(st.session_state.scores) > current_question:
                    st.session_state.scores[current_question] = score
                else:
                    st.session_state.scores.append(score)

                if current_question < len(questions) - 1:
                    st.session_state.current_question += 1
                else:
                    st.session_state.current_question = len(questions)  # Ensure transition to results

    # Show results if quiz is complete
    if current_question == len(questions):
        total_score = sum(st.session_state.scores)
        st.write(f"Ihr Gesamtscore: {total_score}")
        recommendation = next((rec for score_range, rec in recommendations if total_score in score_range), None)
        if recommendation:
            st.write(recommendation)

        # Add a button to restart the quiz
        if st.button("Zurück zur Startseite"):
            st.session_state.quiz_started = False
