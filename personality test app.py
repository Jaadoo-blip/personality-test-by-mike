import streamlit as st

# Custom styling for a modern feel
st.set_page_config(page_title="Personality Profile Quiz", page_icon="🧠")

st.title("🧠 Personality Profile Quiz")
st.markdown("---")

# Data Structure
questions = [
    ("When do you feel at your best?", {"Morning": 2, "Afternoon & early evening": 4, "Late at night": 6}),
    ("You usually walk...", {"Fairly fast, with long steps": 6, "Fairly fast, with little steps": 4, "Less fast, head up": 7, "Less fast, head down": 2, "Very slowly": 1}),
    ("When talking to people, you...", {"Stand with arms folded": 4, "Have hands clasped": 2, "Hands on hips or in pockets": 5, "Touch or push the person": 7, "Touch ear, chin, or hair": 6}),
    ("When relaxing, you sit with...", {"Knees bent, legs side by side": 4, "Legs crossed": 6, "Legs stretched out": 2, "One leg curled under you": 1}),
    ("When something really amuses you, you react with...", {"A big appreciated laugh": 6, "A laugh, but not loud": 4, "A quiet chuckle": 3, "A sheepish smile": 5}),
    ("When you go to a party, you...", {"Make a loud entrance": 6, "Make a quiet entrance": 4, "Make the quietest entrance": 2}),
    ("When you're concentrating and interrupted, you...", {"Welcome the break": 6, "Feel extremely irritated": 2, "Vary between these two": 4}),
    ("Which color do you like most?", {"Red or orange": 6, "Black": 7, "Yellow or light blue": 5, "Green": 4, "Dark blue or purple": 3, "White": 2, "Brown or gray": 1}),
    ("Before going to sleep, you lie...", {"Stretched out on your back": 7, "Face down on stomach": 6, "On your side, slightly curled": 4, "With head on one arm": 2, "With head under covers": 1}),
    ("You often dream that you are...", {"Falling": 4, "Fighting or struggling": 2, "Searching for something": 3, "Flying or floating": 5, "Usually dreamless": 6, "Pleasant dreams": 1})
]

# Initialize state to track answers
if 'answers' not in st.session_state:
    st.session_state.answers = [None] * len(questions)

# Display Questions
for i, (q_text, opts) in enumerate(questions):
    st.subheader(f"Question {i+1}")
    choice = st.radio(q_text, list(opts.keys()), index=None, key=f"q{i}")
    st.session_state.answers[i] = opts[choice] if choice else 0
    st.markdown("---")

# Calculate Result
if st.button("See My Personality Profile", type="primary"):
    if 0 in st.session_state.answers:
        st.warning("Please answer all questions before submitting!")
    else:
        total_score = sum(st.session_state.answers)
        st.success(f"### Your Total Score: {total_score}")
        
        if total_score > 60:
            st.error("**OVER 60 POINTS:** Others see you as someone to 'handle with care.' You're seen as vain, self-centered, and dominant.")
        elif 51 <= total_score <= 60:
            st.warning("**51 TO 60 POINTS:** You're seen as exciting, volatile, and impulsive; a natural leader who is bold and adventuresome.")
        elif 41 <= total_score <= 50:
            st.info("**41 TO 50 POINTS:** Others see you as fresh, lively, and charming. You are the center of attention but stay grounded.")
        elif 31 <= total_score <= 40:
            st.info("**31 TO 40 POINTS:** You're seen as sensible, cautious, and practical. A loyal friend but slow to make new ones.")
        elif 21 <= total_score <= 30:
            st.info("**21 TO 30 POINTS:** Your friends see you as painstaking and fussy. Very cautious and a slow, steady plodder.")
        else:
            st.info("**UNDER 21 POINTS:** People think you are shy and indecisive, someone who needs looking after.")