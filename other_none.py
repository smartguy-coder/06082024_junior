primitives = [1, 22.0, True, False, [], (5,), {}, None]


def create_welcome_message(header: str = '', users: list[str] = None) -> str | None:
    """
    create HTML H1 header according to https://dou.ua/forums/topic/5935/
    """
    if users is None:
        users = []

    # primitives.append(users)
    users.append(header)
    if header:
        return f'<h1>{header}</h1>'
    return


result = create_welcome_message('dghdf', users=[])
result1 = create_welcome_message('555', ['hjhj'])
result2 = create_welcome_message(users=[], header='kjghhjg')


def process_unpacked_data(*args, **kwargs):

    pass


iterable_sec = (1, 2, 88)
first, second, *third = iterable_sec

named_values = {'h': 555, 'value': 99}
process_unpacked_data(22222, *iterable_sec, **named_values)

pass
