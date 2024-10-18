import requests


url = 'https://script.google.com/macros/s/AKfycbz3AYGhyZtqRH-RhjRJB9h-rOSn5ijsTxYasRZNE0xrQIi8Y_Kyr-x8OGeUZ_qOhbqdSA/exec'

response = requests.get(url).json()


