document.addEventListener("DOMContentLoaded", function() {
  const recordButton = document.getElementById("record");
  const stopButton = document.getElementById("stop");
  const audioElement = document.getElementById("audio");
  let mediaRecorder;
  let chunks = [];

  // Start recording
  recordButton.addEventListener("click", async () => {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    mediaRecorder = new MediaRecorder(stream);
    mediaRecorder.start();

    // Enable stop button and disable record button
    stopButton.disabled = false;
    recordButton.disabled = true;

    // Store recorded audio data
    mediaRecorder.ondataavailable = (e) => {
      chunks.push(e.data);
    };

    // Stop recording
    stopButton.addEventListener("click", () => {
      mediaRecorder.stop();
      stopButton.disabled = true;
      recordButton.disabled = false;

      // Create a Blob from recorded audio data and set it as the audio element's source
      const audioBlob = new Blob(chunks, { type: "audio/webm" });
      audioElement.src = URL.createObjectURL(audioBlob);

      // Clear chunks for the next recording
      chunks = [];
    });
  });
});
// send the recorded audio to the server when the form is submitted.
document.querySelector("form").addEventListener("submit", function(event) {
    event.preventDefault();
  
    // Create a FormData object to send the recorded audio
    const formData = new FormData(event.target);
    const audioBlob = new Blob(chunks, { type: "audio/webm" });
  
    // Append the recorded audio to the FormData object
    formData.append("audio_file", audioBlob, "recorded_audio.webm");
  
    // Send the form data to the server using the Fetch API
    fetch(event.target.action, {
      method: "POST",
      body: formData,
    })
      .then((response) => response.text())
      .then((html) => {
        // Replace the page content with the server response
        document.documentElement.innerHTML = html;
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  });
