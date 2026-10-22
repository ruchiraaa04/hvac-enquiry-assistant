
# HVAC Enquiry Assistant
# Day 1: Python fundamentals

business = {
    "name": "CoolCare HVAC Services",
    "services": [
        "AC repair",
        "AC installation",
        "AC maintenance"
    ],
    "service_areas": [
        "Goregaon",
        "Malad",
        "Andheri"
    ],
    "opening_hours": "Monday to Saturday, 9 AM to 6 PM"
}

print(f"Welcome to {business['name']}!")
print("How can we help you today?")
print("Type 'exit' to close the assistant.")

while True:
    message = input("\nYou: ").strip().lower()

    if message == "exit":
        print("Assistant: Thank you for contacting us!")
        break

    elif "service" in message:
        print("Assistant: We offer:")
        for service in business["services"]:
            print(f"- {service}")

    elif "area" in message or "location" in message:
        areas = ", ".join(business["service_areas"])
        print(f"Assistant: Our service areas include {areas}.")

    elif "time" in message or "hours" in message or "open" in message:
        print(f"Assistant: Our hours are {business['opening_hours']}.")

    elif "repair" in message or "not cooling" in message:
        print(
            "Assistant: I can help you with an AC service enquiry. "
            "Please share your location and preferred service date."
        )

    else:
        print(
            "Assistant: I couldn't identify your request. "
            "Please contact our team for assistance."
        )
