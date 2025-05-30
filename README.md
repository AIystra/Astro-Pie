<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/9/99/Astro_Pi_Logo.png" alt="Astro Pi Logo" width="20%"/>
</p>

<h1 align="center">Astro Pi – ISS Speed Estimation Project</h1>
<p align="center">
  🚀 Calculating the International Space Station's orbital speed using images captured by a Raspberry Pi High Quality Camera from orbit.
</p>

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue" alt="Python">
  <img src="https://img.shields.io/github/last-commit/your-username/astro-pi-speed" alt="Last Commit">
  <img src="https://img.shields.io/github/languages/top/your-username/astro-pi-speed" alt="Top Language">
  <img src="https://img.shields.io/badge/Camera-High%20Quality%20Raspberry%20Pi-critical" alt="Camera Type">
</div>

---

<h2>🌌 Project Overview</h2>

<p>
This project was developed for the <strong>European Space Agency's Astro Pi competition</strong>. Its goal is to <strong>estimate the orbital speed of the International Space Station (ISS)</strong> using image processing and computer vision techniques applied to Earth photos taken by the onboard camera.
</p>

---

<h2>🧠 Methodology</h2>

<ol>
  <li>🛰️ <strong>Image Acquisition:</strong> 42 images are captured using the onboard HQ Pi Camera with 9 seconds between each shot.</li>
  <li>📅 <strong>Timestamp Extraction:</strong> The exact capture time is extracted from EXIF metadata, corrected for image writing time.</li>
  <li>🧮 <strong>ORB Feature Matching:</strong> 10,000 keypoints are detected per image pair using OpenCV’s ORB (Oriented FAST and Rotated BRIEF).</li>
  <li>📏 <strong>Distance Estimation:</strong> Matches between image pairs are used to compute average displacement, corrected for radial distortion due to Earth's curvature.</li>
  <li>🌍 <strong>Ground Sampling Distance (GSD):</strong> Calculated using camera specifications and ISS altitude to convert pixel movement into kilometers.</li>
  <li>⚡ <strong>Speed Calculation:</strong> Final speed in km/s is computed based on GSD and corrected time interval.</li>
</ol>

---

<h2>📈 Results</h2>

<ul>
  <li><strong>Baseline (no corrections):</strong> ~7.2 km/s</li>
  <li><strong>With writing time correction:</strong> ~7.4 km/s</li>
  <li><strong>With curvature correction:</strong> ~7.7 km/s</li>
  <li><strong>Improvement:</strong> Accuracy increased by ~4.05%</li>
</ul>

<p>
These refinements bring the calculated speed closer to the actual orbital velocity of the ISS (~7.66 km/s).
</p>

---

<h2>📂 Output</h2>

<p>
Final Result : 7.7285
</p>
<p>
Old Results exported to the folder:
</p>

```txt
test
```
<p> The value is stored with four digits of precision. </p> <h2>📸 Tech Stack</h2> <ul> <li><strong>Language:</strong> Python 3.9+</li> <li><strong>Camera:</strong> Raspberry Pi HQ Camera</li> <li><strong>Libraries:</strong> OpenCV, EXIF, math, datetime, picamzero</li> <li><strong>Environment:</strong> Raspberry Pi / Astro Pi</li> </ul> <h2>🔍 Key Insights</h2> <ul> <li>Ignoring image writing time introduces non-negligible error.</li> <li>Clouds are critical visual markers: 70% of Earth is ocean, making clouds the dominant texture in image matching.</li> <li>Adjusting for Earth curvature refines pixel-based distances significantly.</li> </ul> 

<h2>👁️ Sources</h2>
<p>You can find all the sources we use in the folder :</p>

```txt
test
```

<h2>📜 License</h2> <p>This project is released under the MIT License.</p> <h2>🤝 Acknowledgements</h2> <ul> <li>European Space Agency – <a href="https://astro-pi.org/">Astro Pi Challenge</a></li> <li>Raspberry Pi Foundation</li> <li>ESA Education and Astro Pi Team</li> </ul> 
