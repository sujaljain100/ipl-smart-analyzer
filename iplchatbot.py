import google.generativeai as genai
import pandas as pd

# 1. API Key set karo
genai.configure(api_key="AIzaSyBInLACGZ_nyMhVg2gaSq2i0W6RC6eYyeE")

# 2. IPL Data load karo
matches = pd.read_csv("matches.csv")

# 3. Data ka summary banao AI ke liye
data_summary = f"""
IPL Matches Dataset Summary:
- Total Matches: {len(matches)}
- Seasons: {matches['season'].nunique()}
- Teams: {matches['team1'].unique().tolist()}
- Top Winners: {matches['winner'].value_counts().head(5).to_dict()}
- Player of Match Leaders: {matches['player_of_match'].value_counts().head(5).to_dict()}
"""

# 4. Gemini Model initialize karo
model = genai.GenerativeModel('gemini-1.5-flash-8b')


# 5. Chatbot function
def ask_ipl(question):
    prompt = f"""
    Tu ek IPL Cricket Expert hai.
    Neeche IPL ka data diya hai:
    
    {data_summary}
    
    User ka sawaal: {question}
    
    Short aur clear answer de Hindi/English mein.
    """
    response = model.generate_content(prompt)
    return response.text

# 6. Chat loop
print("🏏 IPL Smart Chatbot - Powered by Gemini AI")
print("Kuch bhi poochho IPL ke baare mein!")
print("Exit karne ke liye 'quit' likho\n")

while True:
    question = input("Tumhara Sawaal: ")
    if question.lower() == 'quit':
        break
    answer = ask_ipl(question)
    print(f"\n🤖 AI: {answer}\n")