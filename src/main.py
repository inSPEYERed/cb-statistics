import json
import os
from datetime import datetime

from dotenv import load_dotenv

from plot_diagrams import plot_bookings_per_week, plot_bookings_per_weekday

load_dotenv()

BASE_FOLDER = './data/'
WP_TABLE_PREFIX = os.getenv('WP_TABLE_PREFIX')
CB_KEYWORDS = ['location-id', 'item-id', 'repetition-start',
               'repetition-end', 'start-time', 'end-time', 'comment']


def parse_posts() -> dict[int, str]:
    print('💠 Parsing posts file')
    with open(os.path.join(BASE_FOLDER, f'{WP_TABLE_PREFIX}_posts.json'), 'r', encoding='utf-8') as f:
        datas = json.loads(f.read())
        datas = datas[2]['data']  # ignore meta information of PHPMyAdmin

    # Group in posts
    posts = {}
    for data in datas:
        if data['post_type'] != 'cb_booking':
            continue
        if data['post_title'] != 'Buchung':
            continue

        post_id = int(data['ID'])
        post_status = data['post_status']

        posts[post_id] = post_status

    return posts


def parse_postmeta() -> dict[int, dict]:
    print('💠 Parsing postmeta file')
    with open(os.path.join(BASE_FOLDER, f'{WP_TABLE_PREFIX}_postmeta.json'), 'r', encoding='utf-8') as f:
        datas = json.loads(f.read())
        datas = datas[2]['data']  # ignore meta information of PHPMyAdmin

    # Group in post_metas (bookings)
    bookings: dict[int, dict] = {}
    for data in datas:
        key = data['meta_key']
        if key not in CB_KEYWORDS:
            continue

        post_id = int(data['post_id'])
        value = data['meta_value']

        # Init empty dict if not there
        if post_id not in bookings:
            bookings[post_id] = {}

        # Add value
        bookings[post_id][key] = value

    return bookings
    # with open(os.path.join(BASE_FOLDER, 'bookings.json'), 'w') as f:
    #     f.write(json.dumps(bookings))


def evaluate_bookings_per_week(bookings: list[dict]) -> dict[int, list[int]]:
    print('💠 Evaluate bookings per week')

    # year -> [count_calender_week_2, count_calender_week_2, ..., count_calender_week_53]
    results: dict[int, list[int]] = {}

    count_other = 0
    count_confirmed = 0
    for booking in bookings:
        # Only bookings that got confirmed
        if booking['status'] != 'confirmed':
            count_other += 1
            continue
        count_confirmed += 1

        # Date
        try:
            start_date_unix = int(booking['repetition-start'])
        except:
            print(
                f'  ❌ Could not find key `repetition-start` in this dataset: {booking}')
            continue

        start_date = datetime.utcfromtimestamp(start_date_unix)
        year = start_date.year
        calender_week = start_date.isocalendar().week

        # Init array for calender weeks
        if year not in results:
            # there are 53 calender weeks per year
            results[year] = [0 for _ in range(53)]

        results[year][calender_week-1] += 1

    print(
        f'  ✅ Confirmed: {count_confirmed}, ❌ Other: {count_other}, Total: {len(bookings)}')
    return results


def evaluate_bookings_per_weekday(bookings: list[dict]) -> dict[int, list[int]]:
    print('💠 Evaluate bookings per weekday')

    # year -> [count_calender_week_2, count_calender_week_2, ..., count_calender_week_53]
    results: dict[int, list[int]] = {}

    count_other = 0
    count_confirmed = 0
    for booking in bookings:
        # Only bookings that got confirmed
        if booking['status'] != 'confirmed':
            count_other += 1
            continue
        count_confirmed += 1

        # Date
        try:
            start_date_unix = int(booking['repetition-start'])
        except:
            print(
                f'  ❌ Could not find key `repetition-start` in this dataset: {booking}')
            continue

        start_date = datetime.utcfromtimestamp(start_date_unix)
        year = start_date.year

        # Monday is 1, Sunday is 7
        weekday = start_date.isocalendar().weekday

        # Init array for calender weeks
        if year not in results:
            # there are 7 weekdays
            results[year] = [0 for _ in range(7)]

        results[year][weekday-1] += 1

    return results


def combine(bookings, bookings_status):
    combined = {}
    no_corresponding_counter = 0
    for id, booking in bookings.items():
        if id not in bookings_status:
            no_corresponding_counter += 1
            # print(
            #     f'❌ Cannot find id {id} in bookings_status, booking dict is: {booking}')
            continue

        status = bookings_status[id]
        combined[id] = {**booking, 'status': status}

    print(
        f'  ❌ Could not find the corresponding booked status data for {no_corresponding_counter} records (out of {len(bookings)})')
    return combined


bookings = parse_postmeta()
bookings_status = parse_posts()
combined = combine(bookings, bookings_status)
# with open('./data/combined.json', 'w') as f:
#     f.write(json.dumps(combined))
combined = list(combined.values())

per_week_results = evaluate_bookings_per_week(combined)
plot_bookings_per_week(per_week_results)

per_weekday_results = evaluate_bookings_per_weekday(combined)
plot_bookings_per_weekday(per_weekday_results)
