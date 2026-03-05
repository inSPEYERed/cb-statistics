function getNumDaysBetween(date1, date2) {
    const difference = date2.getTime() - date1.getTime();
    return Math.ceil(difference / (1000 * 3600 * 24));
}

/**
 * Returns all dates between the start and end date (including start and end date).
 * From https://bobbyhadz.com/blog/javascript-get-all-dates-between-two-dates
 */
function getDatesInRange(startDate, endDate) {
    const date = new Date(startDate);
    const dates = [];
    while (date <= endDate) {
        dates.push(new Date(date));
        date.setDate(date.getDate() + 1);
    }
    return dates;
}

/**
 * Returns ISO-8601 numeric representation of the day of the week:
 * 1 (for Monday) to 7 (for Sunday)
 * From https://www.w3resource.com/javascript-exercises/javascript-date-exercise-22.php
 */
function getIsoWeekday(date) {
    return date.getDay() === 0 ? 7 : date.getDay();
}

/**
 * Returns ISO-8601 week number of year, weeks starting on Monday.
 * First week has number 1.
 * From https://www.w3resource.com/javascript-exercises/javascript-date-exercise-24.php
 */
function getIsoWeekNumber(date) {
    var tdt = new Date(date.valueOf());
    var dayn = (date.getDay() + 6) % 7;
    tdt.setDate(tdt.getDate() - dayn + 3);
    var firstThursday = tdt.valueOf();
    tdt.setMonth(0, 1);
    if (tdt.getDay() !== 4) {
        tdt.setMonth(0, 1 + ((4 - tdt.getDay()) + 7) % 7);
    }
    return 1 + Math.ceil((firstThursday - tdt) / 604800000);
}