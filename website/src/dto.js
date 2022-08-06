class CbData {
    constructor(data) {
        this.title = data['post_title'];
        this.status = data['post_status'];
        this.type = data['type'];
        this.startDate = new Date(data['repetition-start']);
        this.endDate = new Date(data['repetition-end']);
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
        throw 'CSV parser: header is different from the data format we expected';
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