import requests
import json


class ApiCalls:

    def __init__(self):
        pass

    def get(self, url, headers, body):
        r = requests.get(url, headers=headers, data=body)
        return r

    def post(self, url, headers, body):
        r = requests.post(url, headers=headers, data=body)
        return r

    def put(self, url, headers, body):
        r = requests.put(url, headers=headers, data=body)
        return r

    def delete(self, url, headers, body):
        r = requests.delete(url, headers=headers, data=body)
        return r


headers = {}
body = {}
url = "https://restful-booker.herokuapp.com/ping"

r = requests.get(url, headers=headers, data=body)
print(r.status_code)

a = ApiCalls()
our_r = a.get(url, headers, body)

print(our_r.status_code)

url = "https://restful-booker.herokuapp.com/auth"
headers = {'Content-Type': 'application/json'}
body = {"username": "admin", "password": "password123"}

resp_post = a.post(url, headers, body)

print(resp_post.status_code)
#print(resp_post.json())

#for key, value in resp_post.json().items():
#    print(key, ":", value)


url = "https://restful-booker.herokuapp.com/booking"
headers = None
body = None

r_booking_ids = a.get(url, headers, body)

print(r_booking_ids.status_code)
print(r_booking_ids.json())
for value in r_booking_ids.json():
    print(value)
    url = "https://restful-booker.herokuapp.com/booking/" + str(value.get('bookingid'))
    r_booking = a.get(url, headers, body)
    print(r_booking.status_code)
    print(r_booking.json())
