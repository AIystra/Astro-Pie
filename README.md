<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Astro_Pi_Logo.svg/512px-Astro_Pi_Logo.svg.png" alt="Astro Pi Logo" width="15%"/>
</p>

<h1 align="center">Astro Pi – Estimation de la vitesse de l'ISS</h1>
<p align="center">Un projet scientifique basé sur l'analyse d'images capturées depuis la Station Spatiale Internationale</p>

<div align="center">
  <img src="https://img.shields.io/badge/python-3.9%2B-blue.svg" alt="Python 3.9+">
  <img src="https://img.shields.io/badge/status-completed-brightgreen" alt="Status">
  <img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="License">
  <br>
  <img src="https://img.shields.io/github/languages/top/MrCrabs/astro-pi-speed" alt="Top language">
  <img src="https://img.shields.io/github/last-commit/MrCrabs/astro-pi-speed" alt="Last commit">
</div>

---

## 🌌 Objectif du projet

Ce projet, réalisé dans le cadre du concours **Astro Pi – Mission Zero**, a pour objectif d’estimer la **vitesse orbitale de l’ISS** à partir de **42 images successives** prises à intervalles réguliers. Le script utilise des techniques de vision par ordinateur pour mesurer les déplacements de motifs visuels au sol et en déduire la vitesse.

---

## 🧠 Résumé technique

- 📷 Prise de 42 photos avec la caméra PicamZero toutes les 9 secondes.
- ⏱ Extraction des métadonnées EXIF pour récupérer l’heure exacte des prises de vues.
- 🧮 Détection de points caractéristiques avec **ORB** (OpenCV).
- 🧲 Appariement des points et calcul des distances moyennes.
- 🚀 Conversion en vitesse grâce au **Ground Sample Distance (GSD)** fixé à `12648 cm/pixel`.
- 📊 Moyenne de la vitesse sur 41 intervalles pour fiabilité maximale.

---

## 📂 Structure du projet
├── main.py # Script principal
├── result.txt # Fichier de sortie contenant la vitesse finale
├── images/ # Dossier contenant les 42 images capturées


---

## 🔍 Fonctionnalités clés

- Utilisation de **OpenCV ORB** : robustesse en traitement embarqué
- Lecture précise des métadonnées EXIF
- Algorithme de correspondance brute (Brute-Force Matcher)
- Calcul mathématique rigoureux (distance euclidienne → vitesse)
- Moyennage pour éliminer les aberrations visuelles

---

## 📈 Exemple de résultat
Vitesse estimée : 7.7285 km/s

Résultat exporté dans le fichier `result.txt`.

---

## ⚙️ Dépendances

```bash
pip install opencv-python exif
    Python ≥ 3.9

    Modules : cv2, exif, datetime, math, time, picamzero
```
🛰️ Hypothèses et limites

    Le GSD utilisé est une estimation moyenne pour l'altitude de l’ISS.

    Les conditions de prise de vue (nuages, flou) peuvent affecter la détection des points.

    Le modèle suppose une vitesse constante entre chaque photo.

🤝 Remerciements

Merci à la Fondation Raspberry Pi et à l’ESA pour ce concours qui donne l’opportunité aux jeunes de contribuer à la science spatiale à travers le code. 🚀
<p align="center"> <em>Fait avec curiosité et rigueur scientifique par Mr.Crabs 🦀</em> </p> 
