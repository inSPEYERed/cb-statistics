const layout = {
    showlegend: true,
    dragmode: 'pan'
};

const config = {
    scrollZoom: true,
    modeBarButtonsToRemove: ['select2d', 'lasso2d', 'resetScale2d', 'zoomOut2d', 'zoomIn2d'],
    displayModeBar: true
};


function plotBookingsPerWeek(perWeekResults) {
    const calenderWeeks = []
    for (let i = 1; i <= 53; i++) {
        calenderWeeks.push(i);
    }

    // Transform data
    const data = []
    for (const year of Object.keys(perWeekResults)) {
        const yearData = perWeekResults[year];

        const trace = {
            x: calenderWeeks,
            y: Object.values(yearData),
            name: year,
            type: 'bar'
        }
        data.push(trace);
    }

    // Plot
    Plotly.newPlot('plot-bookings-per-week', data,
        {
            ...layout,
            title: 'Buchungen pro Kalenderwoche',
        },
        {
            ...config, toImageButtonOptions: {
                format: 'svg',
                filename: 'Buchungen pro Kalenderwoche'
            }
        });
}

function plotBookingsPerWeekday(perWeekdayResults) {
    const weekdays = ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag', 'Sonntag'];

    // Transform data
    const data = []
    for (const year of Object.keys(perWeekdayResults)) {
        const yearData = perWeekdayResults[year];

        const trace = {
            x: weekdays,
            y: Object.values(yearData),
            name: year,
            type: 'bar'
        }
        data.push(trace);
    }

    // Plot
    Plotly.newPlot('plot-bookings-per-weekday', data,
        { ...layout, title: 'Buchungen pro Wochentag' }, {
        ...config, toImageButtonOptions: {
            format: 'svg',
            filename: 'Buchungen pro Wochentag'
        }
    });
}

function plotBookingsPerItem(perItemResults) {
    // Transform data
    const data = []
    for (const year of Object.keys(perItemResults)) {
        const yearData = perItemResults[year];

        const trace = {
            x: Object.keys(yearData),
            y: Object.values(yearData),
            name: year,
            type: 'bar'
        }
        data.push(trace);
    }

    // Plot
    Plotly.newPlot('plot-bookings-per-item', data,
        { ...layout, title: 'Buchungen pro Item' }, {
        ...config, toImageButtonOptions: {
            format: 'svg',
            filename: 'Buchungen pro Item'
        }
    });
}
