from util_email import send_email, render_html

user_info = {
    'name': 'John',
    "age": 175,
    'hobbies': [
        # 'soccer',
        # 'ping-pong',
        # 'chess',
        # 'tennis'
    ]
}

for hobby in user_info['hobbies']:
    print(hobby)

result = render_html('templates/user_welcome_letter.html', user_info)



send_email(
    ['test_hillel_api_mailing@ukr.net'],
    result,
    'mail subject',
    # 'README.md',
)
