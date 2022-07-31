from datetime import datetime


def get_booking_date(booking: dict[str, str]) -> datetime | None:
    try:
        unix_date = int(booking['repetition-start'])
    except:
        print(f'❌ Could not find key `repetition-start` here: {booking}')
        return None

    return datetime.utcfromtimestamp(unix_date)


def evaluate_bookings_per_week(bookings: list[dict[str, str]]) -> dict[int, list[int]]:
    print('💠 Evaluate bookings per week')

    # year -> [count_calender_week_1, count_calender_week_2, ..., count_calender_week_53]
    results: dict[int, list[int]] = {}

    count_confirmed = 0
    for booking in bookings:
        if booking['status'] != 'confirmed':
            continue
        count_confirmed += 1

        date = get_booking_date(booking)
        if not date:
            continue
        year = date.year
        calender_week = date.isocalendar().week

        if year not in results:
            results[year] = [0 for _ in range(53)]  # 53 calender weeks
        results[year][calender_week-1] += 1
    print(f'{count_confirmed}/{len(bookings)} confirmed bookings')

    return results


def evaluate_bookings_per_weekday(bookings: list[dict[str, str]]) -> dict[int, list[int]]:
    print('💠 Evaluate bookings per weekday')

    # year -> [count_monday, count_tuesday ..., count_sunday]
    results: dict[int, list[int]] = {}

    for booking in bookings:
        if booking['status'] != 'confirmed':
            continue

        date = get_booking_date(booking)
        if not date:
            continue
        year = date.year
        weekday = date.isocalendar().weekday  # Monday is 1, Sunday is 7

        if year not in results:
            results[year] = [0 for _ in range(7)]  # 7 weekdays
        results[year][weekday-1] += 1

    return results


def evaluate_bookings_per_item(bookings: list[dict],
                               items_map: dict[int, str]) -> dict[int, dict[str, int]]:
    print('💠 Evaluate bookings per item')

    # year -> { 'item1': count_item1, 'item2': count_item_2, ... }
    results: dict[int, dict[str, int]] = {}

    for booking in bookings:
        if booking['status'] != 'confirmed':
            continue

        date = get_booking_date(booking)
        if not date:
            continue
        year = date.year

        item = int(booking['item-id'])
        item_name = items_map[item]

        if year not in results:
            results[year] = {}
        try:
            results[year][item_name] += 1
        except KeyError:
            results[year][item_name] = 0

    return results
