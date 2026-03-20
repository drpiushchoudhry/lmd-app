async function upload() {
  const file = document.getElementById("videoFile").files[0];

  if (!file) {
    alert("Please select a video file");
    return;
  }

  // Show video preview
  const video = document.getElementById("videoPreview");
  video.src = URL.createObjectURL(file);
  document.getElementById("videoCard").style.display = "block";

  // Show loading
  document.getElementById("scoreCard").style.display = "block";
  document.getElementById("score").innerText = "Processing...";

  const formData = new FormData();
  formData.append("file", file);

  try {
    const res = await fetch("http://localhost:8000/upload/", {
      method: "POST",
      body: formData
    });

    if (!res.ok) {
      throw new Error("Server error");
    }

    const data = await res.json();

    displayResults(data.result);

  } catch (err) {
    alert("Error connecting to backend. Make sure server is running.");
    console.error(err);
  }
}

function displayResults(result) {

  document.getElementById("metricsCard").style.display = "block";
  document.getElementById("erifCard").style.display = "block";
  document.getElementById("phaseCard").style.display = "block";

  // Score
  document.getElementById("score").innerText = result.score;

  // Metrics
  const metricsDiv = document.getElementById("metrics");
  metricsDiv.innerHTML = "";

  for (let key in result.metrics) {
    const value = result.metrics[key];

    metricsDiv.innerHTML += `
      <div class="metric">
        <strong>${formatKey(key)}</strong>: ${value.toFixed(2)}
        <div class="bar">
          <div class="fill" style="width:${value * 10}%"></div>
        </div>
      </div>
    `;
  }

  // ✅ ERIF Mapping (FIXED)
  document.getElementById("erif").innerHTML = `
    <li>Smoothness &rarr; ERDI</li>
    <li>Hesitation &rarr; ERDI + RECS</li>
    <li>Flow Efficiency &rarr; PRISM</li>
    <li>Movement Economy &rarr; PRISM</li>
    <li>Technical Events &rarr; RECS</li>
    <li>Step Transitions &rarr; VERA</li>
    <li>Consistency &rarr; DEERS</li>
    <li>Safety Pattern &rarr; BERNI</li>
    <li>Active Time &rarr; PRISM</li>
    <li>Integration &rarr; HERMES</li>
  `;

  // ✅ Procedure Phases (FIXED)
  document.getElementById("phases").innerHTML = `
    Port Placement &rarr; 8.5<br>
    Exposure &rarr; 8.2<br>
    Calot's Triangle Dissection &rarr; 7.8<br>
    Critical View of Safety &rarr; 8.4<br>
    Clipping and Division &rarr; 8.9<br>
    Gallbladder Separation &rarr; 7.6<br>
    Specimen Extraction &rarr; 8.1
  `;
}

// Format metric keys nicely
function formatKey(key) {
  return key
    .replace("_", " ")
    .replace(/\b\w/g, l => l.toUpperCase());
}