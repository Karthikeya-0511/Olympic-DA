<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Olympic Project</title>
  <style>
    body {
      font-family: 'Segoe UI', Arial, sans-serif;
      background: #f6f7fb;
      color: #222;
      margin: 0;
      padding: 0;
    }
    .container {
      max-width: 800px;
      margin: 40px auto;
      background: #fff;
      border-radius: 18px;
      box-shadow: 0 4px 24px rgba(0,0,0,0.09);
      padding: 36px 32px 32px 32px;
    }
    .olympic-rings {
      display: flex;
      justify-content: center;
      align-items: center;
      margin-bottom: 18px;
    }
    .ring {
      width: 60px;
      height: 60px;
      border: 6px solid;
      border-radius: 50%;
      margin: 0 5px;
      background: transparent;
      position: relative;
    }
    .ring.blue { border-color: #0081C8; }
    .ring.yellow { border-color: #F4D41E; margin-top: 28px; }
    .ring.black { border-color: #000; }
    .ring.green { border-color: #009F3D; margin-top: 28px; }
    .ring.red { border-color: #DF0024; }

    h1 {
      text-align: center;
      font-size: 2.6rem;
      margin-bottom: 0.2em;
      letter-spacing: 1px;
    }
    .tagline {
      text-align: center;
      font-size: 1.15rem;
      color: #555;
      margin-bottom: 2em;
      font-style: italic;
    }
    h2 {
      color: #0081C8;
      margin-top: 1.8em;
      margin-bottom: 0.5em;
      font-size: 1.45rem;
      letter-spacing: 0.5px;
    }
    ul {
      margin: 0.5em 0 1.5em 1.5em;
      padding: 0;
    }
    li {
      margin-bottom: 0.5em;
      font-size: 1.06rem;
    }
    .highlight {
      background: #f4d41e33;
      padding: 12px 18px;
      border-left: 4px solid #0081C8;
      border-radius: 6px;
      margin-bottom: 1.5em;
    }
    .visuals {
      display: flex;
      gap: 18px;
      flex-wrap: wrap;
      margin-bottom: 1.5em;
    }
    .visual-box {
      flex: 1 1 240px;
      background: #f6f7fb;
      border-radius: 8px;
      padding: 16px;
      text-align: center;
      box-shadow: 0 2px 8px rgba(0,0,0,0.04);
      margin-bottom: 12px;
    }
    .quote {
      font-style: italic;
      color: #555;
      border-left: 4px solid #009F3D;
      padding-left: 14px;
      margin: 2em 0 1em 0;
    }
    @media (max-width: 600px) {
      .container { padding: 16px 5px; }
      .visuals { flex-direction: column; gap: 0; }
    }
  </style>
</head>
<body>
  <div class="container">
    <!-- Olympic Rings -->
    <div class="olympic-rings">
      <div class="ring blue"></div>
      <div class="ring black"></div>
      <div class="ring red"></div>
      <div class="ring yellow"></div>
      <div class="ring green"></div>
    </div>

    <!-- Project Title -->
    <h1>Olympic Project</h1>
    <div class="tagline">Celebrating the spirit, data, and stories of the Olympic Games</div>

    <!-- Overview -->
    <h2>🏅 Overview</h2>
    <div class="highlight">
      Dive into the world of the Olympics! This project analyzes, visualizes, and tells the story of the Games, from Athens 1896 to today. Discover trends, explore medal tallies, and relive iconic moments through data.
    </div>

    <!-- Features -->
    <h2>🌟 Features</h2>
    <ul>
      <li>Interactive visualizations of Olympic history and statistics</li>
      <li>Dynamic medal leaderboards by country and athlete</li>
      <li>Analysis of gender participation and sport evolution</li>
      <li>Modern, responsive web interface</li>
    </ul>

    <!-- Getting Started -->
    <h2>🚀 Getting Started</h2>
    <ul>
      <li>Clone the repository: <code>git clone https://github.com/yourusername/olympic-project.git</code></li>
      <li>Install required dependencies: <code>pip install -r requirements.txt</code></li>
      <li>Launch the app: <code>streamlit run app.py</code></li>
    </ul>

    <!-- Data Sources -->
    <h2>📚 Data Sources</h2>
    <ul>
      <li>Kaggle Olympics Dataset (1896–present)</li>
      <li>International Olympic Committee (IOC) Official Website</li>
    </ul>

    <!-- Visual Highlights -->
    <h2>📊 Visual Highlights</h2>
    <div class="visuals">
      <div class="visual-box">
        <strong>Medal Tally Over Time</strong>
        <br>
        <img src="https://upload.wikimedia.org/wikipedia/commons/7/7c/Medal_table_Olympic_Games_1896-2016.png" alt="Medal Tally" width="100%">
      </div>
      <div class="visual-box">
        <strong>Gender Participation Trends</strong>
        <br>
        <img src="https://upload.wikimedia.org/wikipedia/commons/7/7d/Olympic_Games_gender_participation.png" alt="Gender Participation" width="100%">
      </div>
    </div>

    <!-- Acknowledgements -->
    <h2>🥇 Acknowledgements</h2>
    <ul>
      <li>Inspired by the Olympic spirit and open data community</li>
      <li>Data from Kaggle and the International Olympic Committee</li>
    </ul>

    <div class="quote">
      “The most important thing in the Olympic Games is not winning but taking part.”<br>
      - Pierre de Coubertin
    </div>
  </div>
</body>
</html>
