import requests


URL = 'https://script.google.com/macros/s/AKfycbyEEkTS6wsHhL3cdOZeg_4aZU9j85xsejKnqDsUgSpc7MyVMhHh6n3IHLWKEH70DAwfcw/exec'

response = requests.get(URL)
response_json = response.json()
data = response_json['data']

service_cost_for_electric_cars = 0
japan_cars_quantity = 0

most_expensive_car_in_service = {}
most_expensive_service_cost_per_car = 0

for car_info in data:
    quantity = car_info['quantity']
    service_cost_per_car = car_info['serviceCostPerMonth']
    is_electro = car_info['isElectro']
    country = car_info['country']

    service_cost_total = quantity * service_cost_per_car
    if is_electro:
        service_cost_for_electric_cars += service_cost_total

    if country == 'Японія':
        japan_cars_quantity += quantity

    if service_cost_per_car > most_expensive_service_cost_per_car:
        most_expensive_service_cost_per_car = service_cost_per_car
        most_expensive_car_in_service = car_info

if most_expensive_car_in_service:
    from util_email import send_email, render_html

    result = render_html('templates/car_info_letter.html', most_expensive_car_in_service)

    send_email(
        ['test_hillel_api_mailing@ukr.net'],
        result,
        'Most expensive service car',
        # 'README.md',
    )

















