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
    if (!csv) {
        alert('Could not read the CSV file, check if your browser is up to date and make sure you are able to open the file in Excel. Refresh the page (Ctrl + F5), then try again.');
        return;
    }
    console.log('🙌 Got this CSV');
    console.log(csv);
    console.log('Starting to process the data now...');

    // Parse bookings
    bookings = constructDTOFromCSVArray(csv);
    if (!bookings) {
        console.log('❌ Aborting, CSV reading/parsing not successful');
        return;
    }

    // Do something with the records
    perWeekResults = evaluateBookingsPerWeek(bookings);
    perWeekdayResults = evaluateBookingsPerWeekday(bookings);
    perItemResults = evaluateBookingsPerItem(bookings);

    // Plot
    plotBookingsPerWeek(perWeekResults);
    plotBookingsPerWeekday(perWeekdayResults);
    plotBookingsPerItem(perItemResults);

    $('#plot-div').removeClass('fixed-plot-div-height'); // Rest 0px height
    console.log('Finished ✅');
}
