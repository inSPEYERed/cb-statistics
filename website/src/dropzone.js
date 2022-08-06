// https://web.dev/read-files/#define-drop-zone
// https://stackoverflow.com/a/43378416

let enterTarget = null;

$('#drop-zone').on('dragenter', event => {
    enterTarget = event.target;
    event.stopPropagation();
    event.preventDefault();
    event.originalEvent.dataTransfer.dropEffect = 'copy';
});

$('#drop-zone').on('dragover', event => {
    $('#drop-zone').addClass('drop-active')
    event.stopPropagation();
    event.preventDefault();
});

$('#drop-zone').on('dragleave', event => {
    // https://stackoverflow.com/a/26459269/9655481
    if (enterTarget == event.target) {
        $('#drop-zone').removeClass('drop-active');
        event.stopPropagation();
        event.preventDefault();
    }
});

$('#drop-zone').on('drop', event => {
    $('#drop-zone').removeClass('drop-active');
    event.stopPropagation();
    event.preventDefault();
    const fileList = event.originalEvent.dataTransfer.files;
    console.log(fileList);
    if (fileList.length > 1) {
        alert('Please provide just one single CSV file');
        return;
    }
    file = fileList[0];
    const succeeded = checkMetadataForFile(file);
    if (!succeeded)
        return;



});

function checkMetadataForFile(file) {
    if (file.type) {
        if (file.type != 'text/csv') {
            alert(`Must be a CSV file, but you uploaded this type: ${file.type}`);
            return false;
        }
    } else if (file.name) {
        const extension = file.name.substr(file.name.lastIndexOf('.') + 1);
        if (extension != 'csv') {
            alert(`Must be a CSV file, but you uploaded a file with this extension: ${extension}`);
            return false;
        }
    }
    return true;
}
