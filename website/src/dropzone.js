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
    const files = event.originalEvent.dataTransfer.files;
    handleFiles(files);
});

// https://developer.mozilla.org/en-US/docs/Web/API/File_API/Using_files_from_web_applications#accessing_selected_files_on_a_change_event
$('#input-file').on('change', event => {
    const files = event.target.files;
    handleFiles(files);
});

function handleFiles(files) {
    if (files.length > 1) {
        alert('Please provide just one single CSV file');
        return;
    }
    const file = files[0];

    if (checkMetadataForFile(file)) {
        readCsvFileContent(file);
    }
}

function checkMetadataForFile(file) {
    if (file.type) {
        // Allow CSV and Microsoft Excel CSV
        if (file.type != 'text/csv' && file.type != 'application/vnd.ms-excel') {
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

function readCsvFileContent(file) {
    const reader = new FileReader();
    reader.onload = (event) => {
        const csvText = event.target.result;
        startProcessing(csvText);
    };
    reader.readAsText(file, 'utf-8');
}
