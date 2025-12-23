# City Street Traffic Speed Analysis (EDA Project)

## 1. Introduction

Urban traffic congestion is a major problem in modern cities, leading to increased travel time, fuel consumption, and air pollution. Analyzing traffic speed data helps identify congestion-prone zones and time periods. This project focuses on **Exploratory Data Analysis (EDA)** of city street traffic speeds to understand speed variations and detect congestion zones.

**Course:** Minor 1 – EDA
**Difficulty Level:** Medium

---

## 2. Objectives

* To analyze traffic speed variations across different streets and time periods
* To identify congestion zones based on low average speeds
* To visualize traffic patterns using line plots and heatmaps
* To gain insights that can help in traffic management and urban planning

---

## 3. Dataset Description

The dataset represents traffic speed data collected from multiple city streets at different times.

**Sample Attributes:**

* `Street_ID` – Unique identifier for each street
* `Location` – Area or zone of the city
* `Date` – Date of observation
* `Time` – Time of observation (hourly)
* `Average_Speed (km/h)` – Average vehicle speed
* `Traffic_Density` – Number of vehicles per unit distance (optional)

**Assumption:** Lower average speed indicates higher congestion.

---

## 4. Tools & Technologies Used

* Python
* Jupyter Notebook
* Libraries:

  * Pandas (data manipulation)
  * NumPy (numerical operations)
  * Matplotlib & Seaborn (visualization)

---

## 5. Methodology

### 5.1 Data Collection

Traffic speed data is collected using sensors, GPS data, or traffic monitoring systems placed across different city streets.

### 5.2 Data Cleaning

* Removed missing or null values
* Converted date and time into proper datetime format
* Removed outliers (extremely high or low speeds)

### 5.3 Exploratory Data Analysis (EDA)

EDA is performed to understand:

* Speed distribution
* Time-based speed variations
* Street-wise congestion levels

---

## 6. Data Analysis & Visualizations

### 6.1 Line Plot – Speed Variation Over Time

A line plot is used to show how traffic speed changes during different hours of the day.

**Insight:**

* Morning (8–10 AM) and evening (5–8 PM) show lower speeds due to peak traffic hours.

---

### 6.2 Heatmap – Congestion Zones

A heatmap visualizes average speed across streets and time slots.

**Insight:**

* Darker regions represent lower speeds (high congestion).
* Certain streets consistently show congestion during peak hours.

---

## 7. Congestion Zone Identification

Congestion zones are identified based on a speed threshold.

**Example Rule:**

* Average Speed < 20 km/h → Highly Congested Zone
* Average Speed 20–40 km/h → Moderate Traffic
* Average Speed > 40 km/h → Free Flow Traffic

Using this rule, streets are classified and mapped into congestion categories.

---

## 8. Key Findings

* Traffic congestion is highest during peak office hours
* Commercial and central business areas experience frequent congestion
* Some streets remain congested throughout the day
* Late-night hours show free-flow traffic conditions

---

## 9. Conclusion

This project demonstrates how Exploratory Data Analysis can be used to analyze city traffic speed data effectively. Visual tools like line plots and heatmaps help in easily identifying congestion patterns and problem areas. Such analysis can assist city planners and traffic authorities in improving traffic flow and reducing congestion.

---

## 10. Future Scope

* Real-time traffic analysis using live data
* Predictive modeling for traffic congestion
* Integration with weather and accident data
* Smart traffic signal optimization using AI

---

## 11. References

* Python Documentation
* Pandas & Matplotlib Official Docs
* Urban Traffic Management Research Papers

---

**End of Project**
