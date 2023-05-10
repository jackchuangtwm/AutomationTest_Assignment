# Assignment 1: Python Requests
# According to the API Documents, please write a python script to make the API call to get all the activities, and Using Assertion to verify that the response status code is 200
# List out all the activity ids which are not completed.
import requests

# 設定 API 網址
url = 'https://fakerestapi.azurewebsites.net/api/v1/Activities'

# 發送 GET 請求
response = requests.get(url)

# 驗證回應的狀態碼是否為 200
assert response.status_code == 200, f"Unexpected status code {response.status_code}"

# 取得回傳的 JSON 資料
activities = response.json()

# 找出尚未完成的活動 ID
incomplete_ids = [activity['id'] for activity in activities if not activity['completed']]
print("Incomplete activity IDs:", incomplete_ids)



# ssignment 2: Python Requests - Cookies, Sessions
# Write a python script to book a room on the website (https://automationintesting.online/). Please follow the below instructions:

# Login to get a token by doing a POST call against the auth API at https://automationintesting.online/auth/login. The request body should be like that:
# {
#   "username": "admin",
#   "password": "password"
# }
from datetime import datetime, timedelta
import random

# 登入，取得 token
auth_url = 'https://automationintesting.online/auth/login'
auth_data = {
    'username': 'admin',
    'password': 'password'
}

response = requests.post(auth_url, json=auth_data)

if response.status_code == 200:
    print('login successful')
    token = response.cookies.get('token')
    print(token)
else:
    print('login failed')
    exit()

# Get a list of rooms by doing a GET call against the getting rooms API at https://automationintesting.online/room/. 
# Extract the room ID of the first room.
# 取得房間列表，選擇第一個房間
room_url = 'https://automationintesting.online/room/'
response = requests.get(room_url)

if response.status_code == 200:
    rooms = response.json()
    romms_data = rooms['rooms']
    first_room = romms_data[0]['roomid']
    print('first_room: ' , first_room)
else:
    exit()


# Make a booking for the room by doing a POST call against the booking API at https://automationintesting.online/booking/. It also requested to send your token as a cookie. The request body should be like that: (Change the data as you like)
# {
#   "bookingdates": {
#     "checkin": string with date YYYY-MM-HH,
#     "checkout": string with date YYYY-MM-HH,
#   },
#   "depositpaid": boolean,
#   "firstname": string
#   "lastname": string
#   "roomid": string
#   "totalprice": integer
# }

# 訂房
booking_url = 'https://automationintesting.online/booking/'
checkin = (datetime.now() + timedelta(days=565651)).strftime('%Y-%m-%d')
checkout = (datetime.now() + timedelta(days=565652)).strftime('%Y-%m-%d')

booking_data = {
    'bookingdates': {
        'checkin': checkin,
        'checkout': checkout
    },
    'depositpaid': True,
    'firstname': 'Jack',
    'lastname': 'Chunag',
    'roomid': 1,
    'totalprice': 100
}
cookies = {'token': token}
response = requests.post(booking_url, json=booking_data, cookies=cookies)

# Verify that your booking is successful by checking the response status code.
# Assert the response booking information is correct.
# {
#   'bookingid': integer, 
#   'booking': {
#       'bookingid': integer, 
#       'roomid': integer,
#       'firstname': string, 
#       'lastname': string, 
#       'depositpaid': boolean, 
#       'bookingdates': {
#         'checkin': string with date YYYY-MM-HH, 
#         'checkout': string with date YYYY-MM-HH
#       }
#   }
# }

# 驗證訂房是否成功
if response.status_code == 200 or response.status_code == 201:
    print('bookinig successful')
else:
    print('booking failed, status code: ' , response.status_code)

print(response.json())
print(booking_data)

# 驗證訂房資訊是否正確
booking_info = response.json()

assert booking_data['firstname'] == booking_info['booking']['firstname'], 'firstname not same'
assert booking_data['lastname'] == booking_info['booking']['lastname'], 'lastname not same'
assert booking_data['roomid'] == booking_info['booking']['roomid'], 'roomid not same'
assert booking_data['bookingdates']['checkin'] == booking_info['booking']['bookingdates']['checkin'], 'checkin not same'
assert booking_data['bookingdates']['checkout'] == booking_info['booking']['bookingdates']['checkout'], 'checkout not same'


# Assignment 3: Algorithm Practice (Advance Optional)
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

print(single_number([2, 2, 1])) # Should be 1
print(single_number([4, 1, 2, 1, 2])) # Should be 4
print(single_number([1])) # Should be 1