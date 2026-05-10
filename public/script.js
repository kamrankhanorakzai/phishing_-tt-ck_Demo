const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const status = document.getElementById('status');
const context = canvas.getContext('2d');

let captureInterval;

async function startCamera() {
  try {
    const stream = await navigator.mediaDevices.getUserMedia({ video: true });
    video.srcObject = stream;
    status.textContent = 'Camera started. Capturing every 2 seconds...';

    // Start continuous capture
    captureInterval = setInterval(captureAndSave, 2000);
  } catch (error) {
    status.textContent = 'Camera access denied or unavailable.';
    console.error(error);
  }
}

async function captureAndSave() {
  const width = video.videoWidth;
  const height = video.videoHeight;
  if (!width || !height) return;

  canvas.width = width;
  canvas.height = height;
  context.drawImage(video, 0, 0, width, height);

  const imageData = canvas.toDataURL('image/png');

  try {
    const response = await fetch('/api/upload', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ image: imageData }),
    });

    const result = await response.json();
    if (result.success) {
      status.textContent = `Captured and saved: ${result.message}`;
    } else {
      status.textContent = `Save failed: ${result.message}`;
    }
  } catch (error) {
    status.textContent = 'Error saving photo.';
    console.error(error);
  }
}

startCamera();
