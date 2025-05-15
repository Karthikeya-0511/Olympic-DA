  ![image](https://github.com/user-attachments/assets/c5b3d7ee-0435-4441-a232-3db1d4c9f6f6)



  *Celebrating the spirit, data, and stories of the Olympic Games*
  https://olympic-1b1c61e13773.herokuapp.com/

---

## 🏅 Overview

Welcome to the Olympic Project!  
This repository explores the history, data, and evolution of the Olympic Games, providing insights through interactive visualizations, data analysis, and engaging storytelling. Dive into trends, discover medal tallies, and relive iconic moments through data.

* `athlete_events.csv`: Contains detailed records of athletes and their performances.
* `noc_regions.csv`: Maps NOC (National Olympic Committee) codes to regions.

---

## 🌟 Features

1. **Medal Tally Analysis**

   * Data Cleaning: Filters data for the Summer Olympics, removes duplicates, and handles missing values.
   * Medal Distribution: Calculates the number of Gold, Silver, and Bronze medals won by each country.

2. **Overall Analysis**

   * Key Metrics: Analyzes the number of editions, cities, sports, events, athletes, and nations.
   * Top Countries: Computes the countries with the most medals.

3. **Country-Wise Analysis**

   * Participation Trend: Line plot showing the number of participating countries over time.
   * Successful Countries: Heatmaps for visualizing successful countries in different sports and events.
   * Top Athletes: Lists the most successful athletes based on country or sport.

4. **Visualizations**

   * Uses Plotly and Seaborn for dynamic and interactive data visualizations.
   * Includes line plots, heatmaps, and distribution charts to showcase key findings.

5. **Custom Functions**

   * `fetch_medal_tally(year, country)`: Retrieves medal tally for the specified year and country.
   * `most_successful(df, sport)`: Identifies the most successful athletes in a given sport.
   * `most_successful(df, country)`: Finds the top athletes from a particular country.

## 🚀 How to Run

1. Clone the repository.
2. Install necessary libraries:

   ```bash
   pip install numpy pandas matplotlib seaborn plotly streamlit
   ```
3. Run the Jupyter Notebook:

   ```bash
   jupyter notebook Olympics.ipynb
   ```

## Future Enhancements

* Include data from the Winter Olympics.
* Perform predictive analysis for upcoming events.
* Add interactive dashboards using Plotly Dash.


---


## 📚 Data Sources

- Kaggle Olympics Dataset (1896–present)
- International Olympic Committee (IOC) Official Website


---


## License

This project is licensed under the MIT License.

---


