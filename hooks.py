app_name = "my_clinic_custom"
app_title = "Clinic Customizations"
app_publisher = "Nikolaos Chatziartemiou"
app_description = "Patient Name Formatting"
app_email = "nchatziartemiou@gmail.com"
app_license = "mit"

doc_events = {
    "Patient": {
        "before_save": "my_clinic_custom.patient.format_patient_name"
    }
}