def map_calendar(names: list):
    """
    map data to get common calendar
    Args:
        names: list of name
    Returns:
        list of dict with a form {'day': <day>, 'slots': [<timeslot>]}
    """
    days = list(range(2, 9))
    hours = list(range(0, 25))
    avail_hours = []
    if len(names) != 0:
        names_to_set = set([item['name'] for item in names])

        # get the days where all are available
        map_day = [{'day': di, 'names': set([item['name'] for item in names if item['day'] == di]),
                    'value': [item for item in names if item['day'] == di]} for di in days]
        avail_days = [item for item in map_day if item['names'] == names_to_set]

        # get the time slots where all are available
        for item in avail_days:
            map_hour = [{'slot': hi, 'names': [it['name'] for it in item['value'] if
                                                  it['fromhour'] <= hi and it['tohour'] >= hi]} for hi in hours]
            avail_hours.append({'day': item['day'],
                        'slots': [item['slot'] for item in map_hour if set(item['names']) == names_to_set]})

    return avail_hours
