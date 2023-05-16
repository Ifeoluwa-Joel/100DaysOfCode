"""
Just a file used to explain PyCharm IDE; not relevant to the Coffee Machine Project.
It however, helped me understand nested dictionaries more.
"""

contacts = {
    "James": {
        "phone_number":
            {"WhatsApp": 123456789,
             "Hotline": 124578933},
        "email_address": "james@gmail.com"
    },
    "Jenny": {
        "phone_number": 987654321,
        "email_address": "jenny_gump@gmail.com"
    }
}

jenny_contact = contacts["Jenny"]["phone_number"]
print(jenny_contact)

for key in contacts:
    tel_no = contacts[key]["phone_number"]
    print(f"{key}'s number is {tel_no}")


print(f"James Whatsapp number is {contacts['James']['phone_number']['WhatsApp']}")
print(f"James hotline is {contacts['James']['phone_number']['Hotline']}")
def my_function(n1, n2):
    total = n1 + n2
    return total


my_function(4, 5)
