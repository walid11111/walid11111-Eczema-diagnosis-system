import streamlit as st

# Facts: Symptoms list
universal_symptoms={'rash','itchy_skin','redness','scaling'}
types={'craked skin','burning sensation','Small, itchy blisters on hands or feet',
    'Round, coin-shaped spots','Yellowish, greasy scales','Swelling in lower legs','Intensely itchy'}
symptoms = [
    'rash', 'dry skin', 'cracked skin', 'inflamed_skin', 'blisters',
    'thickened_skin', 'weeping_skin', 'itchy_skin', 'redness', 'scaling','burning sensation','Small, itchy blisters on hands or feet',
    'Round, coin-shaped spots','Yellowish, greasy scales','Swelling in lower legs','Intensely itchy'
]

# Rules for diagnosis
def check_eczema(symptoms_input):
    
    if (len(universal_symptoms.intersection(symptoms_input))==4 )and (len(types.intersection(symptoms_input))==0):#when four universal are there only
        return "Eczema. Cosult a doctor!"
    if len(universal_symptoms.intersection(symptoms_input))<=3:
        return "Not Eczema. Consult a doctor!"
    if universal_symptoms and 'cracked skin' in symptoms_input:
        return "Eczema(Atopic Dermatitis). Consult a doctor!"
    if universal_symptoms and 'burning sensation' in symptoms_input:
        return "Eczema(Contact Dermatitis). Consult a doctor!"
    if universal_symptoms and 'Small, itchy blisters on hands or feet' in symptoms_input:
        return "Eczema(Dyshidrotic Eczema). Consult a doctor!"
    if universal_symptoms and 'Round, coin-shaped spots' in symptoms_input:
        return "Eczema(Nummular Eczema). Consult a doctor!"

    if universal_symptoms and 'Yellowish, greasy scales' in symptoms_input:
        return "Eczema(Seborrheic Dermatitis). Consult a doctor!"
    if universal_symptoms and 'Swelling in lower legs' in symptoms_input:
        return "Eczema(Stasis Dermatitis). Consult a doctor!"
    if universal_symptoms and 'Intensely itchy' in symptoms_input:
        return "Eczema(Neurodermatitis). Consult a doctor!"
# Streamlit UI for input and displaying results
def main():
    st.title("Eczema Diagnosis System")

    # Provide a checklist for symptoms input
    symptoms_input = st.multiselect(
        "Select symptoms you are experiencing:",
        options=symptoms,
        default=[]
    )

    # When user clicks the "Diagnose" button
    if st.button("Diagnose"):
        if symptoms_input:
            # Get the diagnosis based on user input
            diagnosis = check_eczema(symptoms_input)
            st.write(f"Diagnosis: {diagnosis}")
        else:
            st.write("Please select at least one symptom for diagnosis.")

if __name__ == "__main__":
    main()
