async function startProcessing(csvText) {
    // Get CSV
    const csvConfig = {
        'fSep': ';',
        'rSep': '\n',
        'quot': '"',
        'head': false,
        'trim': true
    };
    csv = csvText.csvToArray(csvConfig);
    console.log('▶ Got this CSV');
    console.log(csv);

    // Parse bookings
    bookings = constructDTOFromCSVArray(csv);

    // Do something with the records
    perWeekResults = evaluateBookingsPerWeek(bookings);
    perWeekdayResults = evaluateBookingsPerWeekday(bookings);
    perItemResults = evaluateBookingsPerItem(bookings);

    // Plot
    plotBookingsPerWeek(perWeekResults);
    plotBookingsPerWeekday(perWeekdayResults);
    plotBookingsPerItem(perItemResults);
}
