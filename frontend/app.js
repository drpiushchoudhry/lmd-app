const uploadBtn = document.getElementById("uploadBtn");
const fileInput = document.getElementById("fileInput");
const scoreDiv = document.getElementById("score");

uploadBtn.addEventListener("click", async () => {
    const file = fileInput.files[0];

    if (!file) {
        alert("Please select a video first");
        return;
    }

    scoreDiv.innerHTML = "Analyzing...";

    const formData = new FormData();
    formData.append("file", file);

    try {
        const response = await fetch("https://lmd-backend-piush.onrender.com/analyze", {
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
                "<br>Read Test: " + data.sample_frames_read + " frames";
        }

    } catch (error) {
        console.error(error);
        scoreDiv.innerHTML = "❌ Server error";
    }
});