def get_input(question):
    answer = input(question + " (yes/no): ").lower()
    while answer not in ["yes", "no"]:
        print("Please answer yes or no.")
        answer = input(question + " (yes/no): ").lower()
    return answer == "yes"

def infer_infection():
    print("\n--- Welcome to MYCIN Infection Diagnosis System ---")
    print("Please answer the following questions:")

    fever = get_input("Does the patient have a fever?")
    cough = get_input("Is the patient coughing?")
    chest_pain = get_input("Is there chest pain?")
    sore_throat = get_input("Does the patient have a sore throat?")
    body_ache = get_input("Does the patient experience body ache?")
    rash = get_input("Does the patient have skin rash?")
    diarrhea = get_input("Is the patient experiencing diarrhoea?")

    pus = get_input("Is there pus discharge from a wound?")

    print("\nAnalyzing symptoms...")
    if fever and cough and chest_pain:
        print("Diagnosis: Likely Pneumonia (bacterial)")
    elif fever and sore_throat and body_ache:
        print("Diagnosis: Likely Influenza (viral)")
    elif rash and fever:
        print("Diagnosis: Likely Measles (viral)")
    elif diarrhea and fever:
        print("Diagnosis: Likely Gastroenteritis (viral or bacterial)")
    elif pus and fever:
        print("Diagnosis: Likely Staphylococcal Infection (bacterial)")
    else:
        print("Unable to determine infection with current data. Further tests recommended.")

    print("\n--- End of Diagnosis ---")

if __name__ == "__main__":
    infer_infection()