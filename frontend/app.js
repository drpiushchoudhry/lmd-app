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

        scoreDiv.innerHTML = "Result: " + JSON.stringify(data);

    } catch (error) {
        console.error(error);
        scoreDiv.innerHTML = "Error analyzing video";
    }
});