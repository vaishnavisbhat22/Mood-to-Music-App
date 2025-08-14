import streamlit as st

# Dictionary of moods and songs
mood_songs = {
    "happy": [
        "Happy - Pharrell Williams",
        "Walking on Sunshine - Katrina & The Waves",
        "Best Day of My Life - American Authors"
    ],
    "sad": [
        "Someone Like You - Adele",
        "Fix You - Coldplay",
        "Let Her Go - Passenger"
    ],
    "motivated": [
        "Eye of the Tiger - Survivor",
        "Stronger - Kanye West",
        "Don't Stop Me Now - Queen"
    ],
    "romantic": [
        "Perfect - Ed Sheeran",
        "All of Me - John Legend",
        "A Thousand Years - Christina Perri"
    ]
}

st.title("🎵 Mood-to-Music Recommender")

# Step 1: User selects mood
mood = st.selectbox("Select your mood:", list(mood_songs.keys()))

# Step 2: Show songs
st.write(f"Here are some {mood} songs for you:")
for song in mood_songs[mood]:
    st.write(f"- {song}")


