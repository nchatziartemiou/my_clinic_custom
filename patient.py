import frappe

def format_patient_name(doc, method):
    surname = (doc.last_name or "").strip()
    given = " ".join(filter(None, [doc.first_name, doc.middle_name])).strip()
    
    if surname and given:
        doc.patient_name = f"{surname}, {given}"
    elif surname or given:
        doc.patient_name = surname or given