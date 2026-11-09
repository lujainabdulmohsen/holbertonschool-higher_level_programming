#!/usr/bin/python3

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print(f"Invalid template type: {type(template).__name__}")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Invalid attendees type: expected a list of dictionaries")
        return

    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, 1):
        content = template

        for key in ("name", "event_title", "event_date", "event_location"):
            value = attendee.get(key)
            content = content.replace("{" + key + "}", str(value) if value is not None else "N/A")

        try:
            with open(f"output_{index}.txt", "w") as file:
                file.write(content)
        except OSError as error:
            print(f"Error writing output_{index}.txt: {error}")
