const uploadBtn = document.getElementById("uploadBtn");
const fileInput = document.getElementById("fileInput");
const scoreDiv = document.getElementById("score");

uploadBtn.addEventListener("click", async () => {
    const file = fileInput.files[0];

    if (!file) {
        alert("Please select a video first");
        return;
    }

    scoreDiv.innerHTML = "Analyzing video...";

    const formData = new FormData();
    formData.append("file", file);

    try {
        const response = await fetch("http://127.0.0.1:8000/analyze", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        console.log("Response:", data);

        if (data.status === "error") {
            scoreDiv.innerHTML = "Error: " + data.message;
            return;
        }

        const m = data.metrics;

        scoreDiv.innerHTML = `
            <h3 style="color:#4CAF50;">Analysis Complete</h3>

            <b>Surgical Score:</b> ${data.score}<br><br>

            <b>Video Metrics:</b><br>
            Frames: ${m.frames}<br>
            FPS: ${m.fps}<br>
            Motion Score: ${m.motion_score}<br>
            Frames Sampled: ${m.frames_sampled}<br>
        `;

    } catch (error) {
        console.error("Error:", error);
        scoreDiv.innerHTML = "Error: Cannot connect to backend";
    }
});