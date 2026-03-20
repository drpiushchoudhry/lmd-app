const uploadInput = document.getElementById("fileInput");
const uploadBtn = document.getElementById("uploadBtn");
const scoreBox = document.getElementById("score");
const metricsDiv = document.getElementById("metrics");

const API_URL = "https://lmd-backend-qvsq.onrender.com/upload/";

uploadBtn.addEventListener("click", async () => {
    const file = uploadInput.files[0];

    if (!file) {
        alert("Please select a video");
        return;
    }

    // UX STATES
    scoreBox.innerHTML = `<div class="loader"></div> Uploading video...`;

    setTimeout(() => {
        scoreBox.innerHTML = `<div class="loader"></div> AI analyzing motion...`;
    }, 2000);

    setTimeout(() => {
        scoreBox.innerHTML = `<div class="loader"></div> Computing metrics...`;
    }, 5000);

    const formData = new FormData();
    formData.append("file", file);

    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: {
                "Authorization": "Basic " + btoa("admin:lmd123")
            },
            body: formData
        });

        const data = await response.json();

        const metrics = data.result.metrics;
        const score = data.result.score;

        // FINAL SCORE
        scoreBox.innerHTML = `LMD Score: ${score}`;

        metricsDiv.innerHTML = "";

        for (let key in metrics) {
            let value = metrics[key];

            // Normalize (0–10)
            let ratio = value / 10;

            // Blue → Orange gradient
            let r = Math.floor(59 + ratio * (249 - 59));
            let g = Math.floor(130 + ratio * (115 - 130));
            let b = Math.floor(246 - ratio * (246 - 22));

            let color = `rgb(${r}, ${g}, ${b})`;

            metricsDiv.innerHTML += `
                <div class="metric">
                    <div>${key}: ${value.toFixed(2)}</div>
                    <div class="bar">
                        <div class="fill" style="width:${value * 10}%; background:${color}"></div>
                    </div>
                </div>
            `;
        }

    } catch (err) {
        console.error(err);
        scoreBox.innerHTML = "Error processing video";
    }
});