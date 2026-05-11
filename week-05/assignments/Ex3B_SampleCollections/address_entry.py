# Jordan R. Worrobah
# 5/11/2026
# Address Entry

contact_info = {"address" : "123 Jordans River",
                "city" : "Philadelphia",
                "state" : "PA",
                "zip" : "19147",}

full_name = {"first name" : "Jordan",
             "last name" : "Worrobah",}

full_name.update({"honorific": "Mr."})
contact_info.update({"full_name": full_name})

print(f"The mailing address for {full_name['honorific']} {full_name['first name']} {full_name['last name']} is: ")

print(f"{contact_info['address']}")
print(f"{contact_info['city']}, "
      f"{contact_info['state']} "
      f"{contact_info['zip']}.")