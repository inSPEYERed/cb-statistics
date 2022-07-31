import json
import os

from dotenv import load_dotenv

# Create a .env file that looks like this:
# WP_TABLE_PREFIX=<your-table-prefix, e.g. wp>
print()
print('🔘 Loading environmental variables')
load_dotenv()
load_dotenv()


DATA_FOLDER = './data/'
WP_TABLE_PREFIX = os.getenv('WP_TABLE_PREFIX')
CB_KEYWORDS = ['location-id', 'item-id', 'repetition-start',
               'repetition-end', 'start-time', 'end-time', 'comment']


def read_phpmyadmin_json_file(file: str) -> list[dict]:
    with open(file, 'r', encoding='utf-8') as f:
        records = json.loads(f.read())
        records = records[2]['data']  # ignore meta information of PHPMyAdmin
    return records


def parse_posts_booking_status() -> dict[int, str]:
    print('💠 Parsing posts file -> Extract booking status from it')

    file = os.path.join(DATA_FOLDER, f'{WP_TABLE_PREFIX}_posts.json')
    records = read_phpmyadmin_json_file(file)

    # booking_id -> booking status
    bookings: dict[int, str] = {}
    for record in records:
        if record['post_type'] != 'cb_booking' or record['post_title'] != 'Buchung':
            continue

        id = int(record['ID'])
        status = record['post_status']

        bookings[id] = status

    return bookings


def parse_postmeta_bookings() -> dict[int, dict[str, str]]:
    print('💠 Parsing postmeta file -> Extract booking information from it')

    file = os.path.join(DATA_FOLDER, f'{WP_TABLE_PREFIX}_postmeta.json')
    records = read_phpmyadmin_json_file(file)

    # booking_id -> { cb_key: cb_value, cb_key_2: cb_value_2, ... }
    bookings: dict[int, dict[str, str]] = {}
    for record in records:
        key = record['meta_key']
        if key not in CB_KEYWORDS:
            continue

        id = int(record['post_id'])
        value = record['meta_value']

        try:
            bookings[id][key] = value
        except KeyError:
            bookings[id] = {key: value}

    return bookings


def combine(bookings: dict[int, dict[str, str]],
            bookings_status: dict[int, str]) -> dict[int, dict[str, str]]:
    print('💠 Enriching postmeta json booking information with booking status from posts json')
    combined = {}

    no_match_counter = 0
    for id, booking in bookings.items():
        if id not in bookings_status:
            no_match_counter += 1
            continue

        status = bookings_status[id]
        combined[id] = {**booking, 'status': status}
    print('❌ No corresponding booking status found for ' +
          f'{no_match_counter}/{len(bookings)} records')

    return combined
