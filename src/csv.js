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
    const shouldContain = [
        "post_title",
        "post_status",
        "type",
        "repetition-start",
        "repetition-end",
        "location-post_title",
        "item-post_title",
        "user-firstname",
        "user-lastname",
        "user-login",
        "comment"
    ];
    return headerArray.length >= shouldContain.length
        && shouldContain.every((key) => headerArray.includes(key))  ;
}
