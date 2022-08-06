function evaluateBookingsPerWeek(bookings) {
    results = {};
    for (const booking of bookings) {
        if (booking['status'] != 'confirmed')
            continue;

        const year = booking.startDate.getFullYear();
        if (!(year in results)) {
            results[year] = []
            // Init 53 calender weeks
            for (let i = 0; i < 53; i++) {
                results[year].push(0);
            }
        }

        const dates = getDatesInRange(booking.startDate, booking.endDate);
        for (const date of dates) {
            const weekNumber = getIsoWeekNumber(date);
            results[year][weekNumber - 1] += 1;
        }
    }
    return results;
}

function evaluateBookingsPerWeekday(bookings) {
    results = {};
    for (const booking of bookings) {
        if (booking['status'] != 'confirmed')
            continue;

        const year = booking.startDate.getFullYear();
        if (!(year in results))
            results[year] = [0, 0, 0, 0, 0, 0, 0] // Monday to Sunday

        const dates = getDatesInRange(booking.startDate, booking.endDate);
        for (const date of dates) {
            const weekDay = getIsoWeekday(date);
            results[year][weekDay - 1] += 1;
        }
    }
    return results;
}

function evaluateBookingsPerItem(bookings) {
    results = {};
    for (const booking of bookings) {
        if (booking['status'] != 'confirmed')
            continue;

        const year = booking.startDate.getFullYear();
        const numDates = getNumDaysBetween(booking.startDate, booking.endDate);
        const numBookingDates = numDates + 1;
        const item = booking.item;

        if (!(year in results))
            results[year] = {};

        if (item in results[year]) {
            results[year][booking.item] += numBookingDates;
        } else {
            results[year][booking.item] = numBookingDates;
        }
    }
    return results;
}
