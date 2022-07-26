const fasta1 = document.getElementById('fasta_1');
const fasta2 = document.getElementById('fasta_2');
const labelfasta1 = document.getElementById('alert_seq1_fasta1');
const labelfasta2 = document.getElementById('alert_seq2_fasta2');

fasta1.addEventListener('change', (event) => {
    const fastadoc1 = event.target.files[0];
    if (!fastadoc1) {
        return;
    }
    var reader = new FileReader();
    reader.readAsText(fastadoc1);
    reader.onload = function () {
        text = reader.result;
        var lines = text.split('\n');
        header = lines[0];
        seq = lines[1].replace(/\s/g, '').substring(0, 60);
        labelfasta1.innerHTML = 'Organismo: ' + header.split('|')[4].split(',')[0] + '<br>' + 'Secuencia: ' + 'Id: ' + header.split('|')[1]; + seq + '<br>'
    };
});

fasta2.addEventListener('change', (event) => {
    const fastadoc2 = event.target.files[0];
    if (!fastadoc2) {
        return;
    }
    var reader2 = new FileReader();
    reader2.readAsText(fastadoc2);
    reader2.onload = function () {
        text2 = reader2.result;
        var lines2 = text2.split('\n');
        header2 = lines2[0];
        seq2 = lines2[1].replace(/\s/g, '').substring(0, 60);
        labelfasta2.innerHTML = 'Organismo: ' + header2.split('|')[4].split(',')[0] + '<br>' + 'Secuencia: ' + 'Id: ' + header2.split('|')[1]; + seq2 + '<br>'
    };
});