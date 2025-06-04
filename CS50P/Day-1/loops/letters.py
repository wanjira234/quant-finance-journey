def main():
    names = ["luigi", "mario", "yoshi", "daisy", "peach"]
    for name in names:
        print(write_letter(name, "Princess peach"))

def write_letter(reciever, sender):
    return f"""
   +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    Dear {reciever},

    You are cordially invited to a ball at Peach's castle at 7:00 PM {sender}.
    Sincerely,
    {sender}
   +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    """
main()

