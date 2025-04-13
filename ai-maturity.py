import streamlit as st
from PIL import Image

st.set_page_config(page_title="AI Maturity Scan", layout="centered")

# Add logo
try:
    logo = Image.open("images/logo.png")
    st.image(logo, width=200)  # Adjust width as needed
except:
    st.warning("Logo image not found. Please add a logo.png file to the images directory.")

st.title("🤖 AI Maturity Quickscan")

questions_and_options = [
    ("Hoeveel tijd kan uw organisatie vrijmaken voor AI-initiatieven?", [
        "A. We hebben beperkte tijd en middelen; AI is nog een nieuwe uitdaging.",
        "B. Er is enige ruimte en budget beschikbaar, maar we moeten prioriteiten stellen.",
        "C. We hebben ruime middelen en een toegewijd team om AI volledig te integreren."
    ]),
    ("Zijn er binnen uw organisatie interne teams of externe partners met AI-kennis?", [
        "A. Nee, we moeten AI-expertise nog opbouwen.",
        "B. We hebben een beperkt aantal experts of toegang tot externe ondersteuning.",
        "C. Ja, we hebben sterke interne en externe AI-capaciteiten."
    ]),
    ("Hoe groot is de betrokkenheid van het leiderschap bij AI-initiatieven?", [
        "A. Het leiderschap is voorzichtig en heeft AI (nog) niet als prioriteit gesteld.",
        "B. Het leiderschap toont interesse en ondersteunt enkele initiatieven.",
        "C. Het leiderschap is een actieve sponsor van AI-projecten en stimuleert innovatie."
    ]),
    ("Is er een breed draagvlak binnen de organisatie voor AI?", [
        "A. Niet echt; veel collega's zijn nog onvoldoende vertrouwd met de mogelijkheden en risico's van AI.",
        "B. Redelijk; sommige afdelingen tonen enthousiasme, maar niet iedereen is overtuigd.",
        "C. Ja, AI wordt breed gedragen en er is enthousiasme om er mee aan de slag te gaan."
    ]),
    ("Hoe sterk worden AI-oplossingen/-initiatieven momenteel ingezet om de strategische doelstellingen van uw organisatie te ondersteunen?", [
        "A. AI speelt nog geen rol in het realiseren van onze strategie.",
        "B. AI begint een plaats te krijgen in onze strategische planning.",
        "C. AI is een integraal onderdeel van onze strategie en processen."
    ]),
    ("Wat is het huidige niveau van AI-toepassingen binnen uw organisatie?", [
        "A. We hebben nog geen AI toegepast in onze interne processen of externe dienstverlening.",
        "B. We hebben enkele piloten of use cases getest (in een sandbox omgeving), met wisselend succes.",
        "C. We hebben meerdere succesvolle projecten en toepassingen geïmplementeerd."
    ])
]

st.write("Beantwoord elke vraag door een keuze te maken:")

answers = []

for i, (question, opts) in enumerate(questions_and_options):
    st.markdown(f"**{i+1}. {question}**")  # Make question bold
    answer = st.radio("", opts, key=f"q{i}")  # Empty label since question is shown above
    answers.append(answer[0])  # Enkel de letter A/B/C

# Tel de antwoorden
a_count = answers.count("A")
b_count = answers.count("B")
c_count = answers.count("C")

if st.button("🔍 Toon resultaat"):
    st.markdown("---")
    st.subheader("📊 Resultaat:")
    st.write(f"Aantal A-antwoorden: {a_count}")
    st.write(f"Aantal B-antwoorden: {b_count}")
    st.write(f"Aantal C-antwoorden: {c_count}")

    if a_count > b_count and a_count > c_count:
        st.success("Je organisatie zit in de **AI Explorer** fase. Tijd om te verkennen en leren!")
    elif b_count > a_count and b_count > c_count:
        st.info("Je organisatie bevindt zich in de **AI Pilot** fase. Goed bezig met experimenteren!")
    elif c_count > a_count and c_count > b_count:
        st.success("Gefeliciteerd! Je organisatie is een **AI Expert** – strategisch en geïntegreerd bezig met AI.")
    else:
        st.warning("Er is een gelijke score. Kijk samen met je team welke richting het meest herkenbaar is.")
