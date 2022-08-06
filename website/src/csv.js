// function getCsv() {
//     const csvConfig = {
//         'fSep': ';',
//         'rSep': '\n',
//         'quot': '"',
//         'head': false,
//         'trim': true
//     };

//     return new Promise((resolve, reject) => {
//         $.ajax({
//             url: '/data/cb-export.csv',
//             dataType: 'text',
//             cache: false,
//             success: data => {
//                 csvArray = data.csvToArray(csvConfig);
//                 resolve(csvArray);
//             },
//             error: error => {
//                 reject(error);
//                 console.log(csvArray);
//             }
//         });
//     });
// }

function isExpectedHeader(headerArray) {
    const expectedHeader = [
        "ID",
        "post_author",
        "post_date",
        "post_date_gmt",
        "post_content",
        "post_title",
        "post_excerpt",
        "post_status",
        "post_name",
        "type",
        "timeframe-repetition",
        "grid",
        "timeframe-max-days",
        "full-day",
        "repetition-start",
        "repetition-end",
        "start-time",
        "end-time",
        "pickup",
        "return",
        "booking-code",
        "location-post_title",
        "item-post_title",
        "user-firstname",
        "user-lastname",
        "user-login",
        "comment"
    ];
    return headerArray.length === expectedHeader.length
        && headerArray.every((value, index) => value === expectedHeader[index]);
}
