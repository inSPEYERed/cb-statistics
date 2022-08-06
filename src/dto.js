class CbData {
    constructor(data) {
        this.title = data['post_title'];
        this.status = data['post_status'];
        this.type = data['type'];

        // Dates
        const beginDateStr = convertToParsableDateString(data['repetition-start']);
        const endDateStr = convertToParsableDateString(data['repetition-end']);
        this.startDate = new Date(beginDateStr);
        this.endDate = new Date(endDateStr);

        this.station = data['location-post_title'];
        this.item = data['item-post_title'];
        this.user = new User({
            firstname: data['user-firstname'],
            lastname: data['user-lastname'],
            loginname: data['user-login']
        });
        this.comment = data['comment'];
    }
}

class User {
    constructor(user) {
        this.firstname = user.firstname;
        this.lastname = user.lastname;
        this.loginname = user.loginname;
    }
}

function constructDTOFromCSVArray(csv) {
    // Header
    header = csv[0];
    if (!isExpectedHeader(header)) {
        alert('CSV parser: unexpected header, is this data from a Commons Booking export?');
        return null;
    }

    // Construct DTOs
    bookings = []
    for (const row of csv.slice(1)) {
        // Temporary map
        const data = {};
        for (let i = 0; i < header.length; i++) {
            const key = header[i];
            const value = row[i];
            data[key] = value;
        }
        booking = new CbData(data);
        bookings.push(booking);
    }

    return bookings
}

function convertToParsableDateString(dateStr) {
    // Commons Booking has this format: 25. May 2022
    // we get back: 25 May 2022 (this is parsable by Date.parse())
    return dateStr.replaceAll('.', '');
}