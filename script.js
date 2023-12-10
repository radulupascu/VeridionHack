let recordButton = document.getElementById("recordButton");
let searchLabelButton = document.getElementById("searchLabelButton");
let audioPlayback = document.getElementById("audioPlayback");
let timeBar = document.getElementById("timeBar");

let mediaRecorder;
let audioChunks = [];
let maxRecordingTime = 30000; // 30 seconds
let updateInterval = 100; // Update the time bar every 100ms
let recordingTimeout;
let interval;

recordButton.addEventListener("click", function() {
    navigator.mediaDevices.getUserMedia({ audio: true })
        .then(stream => {
            mediaRecorder = new MediaRecorder(stream);
            mediaRecorder.start();

            recordButton.classList.add('recording');
            searchLabelButton.disabled = false;
            recordButton.disabled = true;

            audioChunks = [];
            timeBar.style.width = '0%';
            let startTime = Date.now();

            interval = setInterval(() => {
                let elapsedTime = Date.now() - startTime;
                let widthPercentage = (elapsedTime / maxRecordingTime) * 100;
                timeBar.style.width = widthPercentage + '%';

                if (elapsedTime >= maxRecordingTime) {
                    clearInterval(interval);
                    stopRecording();
                }
            }, updateInterval);

            mediaRecorder.addEventListener("dataavailable", event => {
                audioChunks.push(event.data);
            });

            mediaRecorder.addEventListener("stop", () => {
                let audioBlob = new Blob(audioChunks);
                let audioUrl = URL.createObjectURL(audioBlob);
                audioPlayback.src = audioUrl;
            });
        });
});

searchLabelButton.addEventListener("click", function() {
    stopRecording(); // Ensure recording is stopped
    window.location.href = "labels.html"; // Redirect to labels.html
});

function stopRecording() {
    if (mediaRecorder && mediaRecorder.state !== 'inactive') {
        mediaRecorder.stop();
        clearInterval(interval);
        recordButton.disabled = false;
        searchLabelButton.disabled = true;
        recordButton.classList.remove('recording');
    }
}
