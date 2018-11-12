def validate_time(list_data: list):
    """
    validate if time is not even
    Args:
        list_data: list of data
    Returns:
        dict {'code': <200 or failed code 415>, 'response': <either list of data or failed message>}
    """
    out = dict(code=200, response=list_data)
    validate_data = [item for item in list_data if isinstance(item['fromhour'], int) and isinstance(item['fromhour'], int)]
    if len(validate_data) != len(list_data):
        out = dict(code=415, response='The time should be even')
    return out


def map_calendar(list_data: list):
    """
    map data to get common calendar
    Args:
        list_data: list of data
    Returns:
        list of dict with a form {'day': <day>, 'slots': [<timeslot>]}
    """
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    hours = list(range(0, 25))
    avail_hours = []
    if len(list_data) != 0:
        names_to_set = set([item['name'] for item in list_data])

        # get the days in which all are available
        map_day = [{'day': di, 'names': set([item['name'] for item in list_data if item['day'] == di]),
                    'value': [item for item in list_data if item['day'] == di]} for di in days]
        avail_days = [item for item in map_day if item['names'] == names_to_set]

        # get the time slots from the days in which all are available
        for item in avail_days:
            map_hour = [{'slot': hi, 'names': [it['name'] for it in item['value'] if
                                                  it['fromhour'] <= hi and it['tohour'] >= hi]} for hi in hours]
            avail_hours.append({'day': item['day'],
                        'slots': [item['slot'] for item in map_hour if set(item['names']) == names_to_set]})

    return avail_hours
