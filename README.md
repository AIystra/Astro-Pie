<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Astro Pi — Vitesse de l'ISS</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 2rem;
            background-color: #f9f9f9;
            color: #333;
        }
        h1, h2, h3 {
            color: #1f3c88;
        }
        code, pre {
            background-color: #efefef;
            padding: 0.2em 0.4em;
            border-radius: 4px;
            font-size: 0.95em;
        }
        section {
            margin-bottom: 2rem;
        }
        .result {
            background: #e8f4ff;
            border-left: 5px solid #1f3c88;
            padding: 1em;
            margin-top: 1rem;
            font-family: monospace;
        }
    </style>
</head>
<body>

    <header>
        <h1>🚀 Astro Pi — Mesure de la Vitesse Orbitale de l’ISS</h1>
        <p><strong>Auteur :</strong> Mr.Crabs<br>
           <strong>Projet :</strong> Concours Astro Pi – Mission Zero<br>
           <strong>Langage :</strong> Python 3<br>
           <strong>Librairies :</strong> OpenCV, EXIF, Picamzero
        </p>
    </header>

    <section>
        <h2>🎯 Objectif du Projet</h2>
        <p>Ce projet vise à estimer la vitesse orbitale de la Station Spatiale Internationale (ISS) à partir d’une série de 42 images prises avec la caméra PicamZero. Le traitement d’image permet de détecter les déplacements de points caractéristiques entre chaque image, puis de les convertir en vitesse grâce à la distance échantillonnée au sol (GSD).</p>
    </section>

    <section>
        <h2>🧪 Méthodologie</h2>
        <ol>
            <li>Prise de 42 photos espacées de 9 secondes via <code>picamzero</code>.</li>
            <li>Extraction des métadonnées EXIF pour obtenir les timestamps précis.</li>
            <li>Utilisation d’<code>ORB</code> (OpenCV) pour détecter les points clés sur chaque image.</li>
            <li>Appariement des descripteurs entre images successives.</li>
            <li>Calcul de la distance moyenne des déplacements.</li>
            <li>Conversion en kilomètres à partir du GSD (12648 cm/pixel).</li>
            <li>Calcul de la vitesse moyenne sur les 41 paires d’images.</li>
        </ol>
    </section>

    <section>
        <h2>🔬 Avancées Techniques</h2>
        <ul>
            <li>📌 Détection robuste avec ORB adaptée à un environnement embarqué.</li>
            <li>📅 Précision temporelle grâce aux balises EXIF.</li>
            <li>📏 Modélisation rigoureuse du déplacement pixel ↔ terrain avec GSD.</li>
            <li>📈 Moyennage statistique pour lisser les imprécisions locales.</li>
        </ul>
    </section>

    <section>
        <h2>📁 Structure du Code</h2>
        <pre><code>instruction()               # Fonction principale
get_time(), get_time_diff() # Extraction des métadonnées temporelles
calculate_features()        # Détection de points ORB
calculate_matches()         # Appariement descripteurs
find_matching_coordinates() # Coordonnées de correspondance
calculate_mean_distance()   # Moyenne des déplacements
calculate_speed_in_kmps()   # Conversion pixel ↔ vitesse
</code></pre>
    </section>

    <section>
        <h2>🧾 Exemple de Résultat</h2>
        <p>La vitesse finale est écrite dans un fichier <code>result.txt</code>.</p>
        <div class="result">
            7.6432
        </div>
        <p><em>La vitesse est exprimée en kilomètres par seconde (km/s).</em></p>
    </section>

    <section>
        <h2>⚙️ Dépendances</h2>
        <pre><code>pip install opencv-python exif</code></pre>
        <p>Librairies natives utilisées : <code>math</code>, <code>datetime</code>, <code>time</code></p>
    </section>

    <section>
        <h2>🛰️ Hypothèses & Limites</h2>
        <ul>
            <li>GSD fixé à 126.48 m/pixel, valeur moyenne estimée.</li>
            <li>Supposition que l’ISS se déplace à vitesse constante sur de courtes périodes.</li>
            <li>Résultats sensibles au flou de mouvement ou aux erreurs d’appariement.</li>
        </ul>
    </section>

    <section>
        <h2>🤝 Remerciements</h2>
        <p>Merci à la Fondation Raspberry Pi et à l’ESA pour ce programme éducatif qui permet aux jeunes de contribuer à des expériences scientifiques réelles dans l’espace.</p>
    </section>

    <footer>
        <hr>
        <p>&copy; 2025 — Mr.Crabs | Projet soumis dans le cadre d’Astro Pi Mission Zero</p>
    </footer>

</body>
</html>
