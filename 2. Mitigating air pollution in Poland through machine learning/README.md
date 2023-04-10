# Mitigating Air Pollution in Poland Through Machine Learning

## Problem Statement

### Background

According to the Air Quality in Europe 2022 report by the European Environment Agency (EEA), air pollution is the largest environmental health risk in Europe and significantly impacts the health of the European population. There are several types of compounds considered as air pollutants. On the one hand, there is particulate matter (PM) of different sizes (PM2.5, PM10) consisting of solid and liquid particles suspended in air. On the other hand, also common gases, such as nitrogen dioxide (NO2), carbon dioxide (CO2), or ozone (O3), contribute to air pollution. The different pollutant quantities can further be combined into a single air quality index, such as the common air quality index (CAQI) used in the European Union.

### Problem

Air pollution is a particular problem in Poland. The annual EEA reports on air quality show that Poland is among the countries with the worst air quality in Europe. Bad air quality affects people's lives and constitutes a considerable health risk. Therefore, mitigating air pollution could improve quality of life and lead to an overall healthier society. At the same time, this would reduce costs for the Polish health care system.

An important step towards mitigation is the identification of main factors and causes of air pollution specific to Poland. By using local time-series data on air pollutants together with other relevant country-specific data, an AI assisted approach could yield valuable insights in this matter. In particular, a machine-learning model for air quality prediction could give policy makers a simple but powerful tool to help tackle the issue of air pollution in Poland.

### Project Goals

* Identification of main factors contributing to air pollution in Poland
* Prototype a simple machine-learning model to predict air quality (classification or regression model, conventional or deep learning model)
* Open source GitHub repository

## Task overview

* **Task 1 - Data Cleaning:**
    * Clean and combine data files from the provided sources
    * obtain three tabular datasets for (i) pollutant data, (ii) weather data, and (iii) general regional data


* **Task 2 - Data Preprocessing:**
    * Merge locations of measurement stations for pollutants and weather appropriately
    * Combine them with the general regional data
    * Obtain a single tabular data file that can be used for EDA and modelling
    

* **Task 3 - EDA:**
    * Data visualization and time-series analysis
    * pin down main causes and possible hotspots of air pollution


* **Task 4 - Modelling:**
    * Develop a machine-learning model to predict air quality based on the given features
    * Use the trained model to analyze feature importance to identify main factors contributing to air pollution in Poland
    * Forecast future air quality levels using the chosen model.