import pandas as pd
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
df = pd.read_csv('PokemonDatabase.csv')
dataset_text = df.head(10).to_string()

prompt = f"""
I have a dataset about Pokemon here:
{dataset_text}

Requirements:
Check if the predict model of Pokemon right or wrong
"""

print("Sending data to Groq for analysis... Please wait.")

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": prompt}]
)

print("\n========== REPORT FROM GROQ ==========\n")
print(response.choices[0].message.content)

df["Base Stat Total"] = df["Health Stat"] + df["Attack Stat"] + df["Defense Stat"] + df["Special Attack Stat"] + df["Special Defense Stat"] + df["Speed Stat"]

strongest_pokemon = df.loc[df["Base Stat Total"].idxmax()]

print("Strongest Pokémon:")
print(strongest_pokemon)