import streamlit as st
import random

# Page config
st.set_page_config(page_title="Stone Paper Scissors", page_icon="🎮")

st.title("🎮 Stone Paper Scissors Game")
st.markdown("### 🎯 First to 5 wins!")

# Initialize session state
if "user_score" not in st.session_state:
    st.session_state.user_score = 0
if "comp_score" not in st.session_state:
    st.session_state.comp_score = 0
if "history" not in st.session_state:
    st.session_state.history = []

choices = {1: "🪨 Stone", 2: "📄 Paper", 3: "✂️ Scissor"}

# Score display
st.subheader(f"Your Score: {st.session_state.user_score} | Computer Score: {st.session_state.comp_score}")

# Buttons
col1, col2, col3 = st.columns(3)

user_choice = None

if col1.button("🪨 Stone"):
    user_choice = 1
elif col2.button("📄 Paper"):
    user_choice = 2
elif col3.button("✂️ Scissor"):
    user_choice = 3

# Game logic
if user_choice:
    computer = random.randint(1, 3)

    st.write(f"You chose **{choices[user_choice]}**")
    st.write(f"Computer chose **{choices[computer]}**")

    if user_choice == computer:
        st.info("🤝 It's a tie!")

    elif (user_choice == 1 and computer == 3) or \
         (user_choice == 2 and computer == 1) or \
         (user_choice == 3 and computer == 2):

        st.success("🎉 You win this round!")
        st.session_state.user_score += 1

    else:
        st.error("💻 Computer wins this round!")
        st.session_state.comp_score += 1

    # Save history
    st.session_state.history.append(
        f"You: {choices[user_choice]} | Computer: {choices[computer]}"
    )

# Win condition
if st.session_state.user_score == 5:
    st.balloons()
    st.success("🏆 Congratulations! You won the game!")

if st.session_state.comp_score == 5:
    st.error("💻 Computer won the game!")

# Restart button
if st.button("🔄 Restart Game"):
    st.session_state.user_score = 0
    st.session_state.comp_score = 0
    st.session_state.history = []

# Game history
st.subheader("📜 Game History")
for h in st.session_state.history[-5:]:
    st.write(h)

# Win rate
total = st.session_state.user_score + st.session_state.comp_score
if total > 0:
    win_rate = (st.session_state.user_score / total) * 100
    st.write(f"📊 Win Rate: {win_rate:.2f}%")