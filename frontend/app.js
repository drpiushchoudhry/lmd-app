const uploadBtn = document.getElementById("uploadBtn");
const fileInput = document.getElementById("fileInput");
const scoreDiv = document.getElementById("score");

uploadBtn.addEventListener("click", async () => {
    const file = fileInput.files[0];

    if (!file) {
        alert("Please select a video");
        return;
    }

    scoreDiv.innerHTML = "Analyzing...";

    const formData = new FormData();
    formData.append("file", file);

    try {
        const response = await fetch("http://127.0.0.1:8000/analyze", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        if (data.status === "error") {
            scoreDiv.innerHTML = "❌ " + data.message;
        } else {
            scoreDiv.innerHTML =
                "✅ Frames: " + data.frames +
                "<br>FPS: " + data.fps +
                "<br>Test frames: " + data.sample_frames;
        }

    } catch (err) {
        scoreDiv.innerHTML = "❌ Backend not running";
    }
});