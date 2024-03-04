from faker import Faker
import json

fake = Faker()

alldata = {'records': []}

for x in range(1000):
    data = {
        "name": fake.name(),
        "age": fake.random_int(min=18, max=80, step=1),
        "street": fake.street_address(),
        "city": fake.city(),
        "zip": fake.zipcode(),
        "lng": float(fake.longitude()),
        "lat": float(fake.latitude())
    }
    alldata['records'].append(data)

# Open the file in write mode and use json.dump() to write the data
with open('data2.json', 'w') as output_file:
    json.dump(alldata, output_file, indent=4)

print("Data written to data.json successfully!")
