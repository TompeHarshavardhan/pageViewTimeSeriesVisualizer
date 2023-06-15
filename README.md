# FreeCodeCamp Forum Page Views Visualization

The FreeCodeCamp Forum Page Views Visualization project aims to analyze and visualize time series data using line charts, bar charts, and box plots. The dataset used in this project contains the number of page views each day on the FreeCodeCamp.org forum from May 9, 2016, to December 3, 2019. By visualizing the data, we can identify patterns, trends, and growth on a yearly and monthly basis.

## Introduction

The project involves importing the dataset using Pandas, cleaning the data by filtering out extreme values, and creating various data visualizations using Matplotlib and Seaborn. The visualizations include a line chart representing daily page views over the specified time period, a bar chart showing average daily page views for each month grouped by year, and box plots illustrating the distribution of page views on a yearly and monthly basis.

## Project Tasks

The main tasks performed in this project include:

1. Data Import: Using Pandas to import the data from the "fcc-forum-pageviews.csv" file and setting the index to the date column.
2. Data Cleaning: Filtering out days with page views in the top 2.5% and bottom 2.5% of the dataset to remove outliers.
3. Line Chart: Creating a line chart using Matplotlib to represent the daily page views over the time period from May 2016 to December 2019.
4. Bar Chart: Drawing a bar chart using Matplotlib to display the average daily page views for each month grouped by year.
5. Box Plots: Utilizing Seaborn to create two adjacent box plots to visualize the distribution of page views on a yearly and monthly basis.
6. Chart Titles and Labels: Providing appropriate titles and labels for each chart to enhance clarity and understanding.

## Project Files

The project includes the following files:

- `time_series_visualizer.py`: The main Python script that performs data import, data cleaning, and visualization tasks.
- `fcc-forum-pageviews.csv`: The dataset file in CSV format containing the daily page views on the FreeCodeCamp.org forum.
- `test_module.py`: Unit test file to validate the correctness of the implemented functions.


## Running the Unit Tests

Unit tests are available in the `main.py` file to verify the correctness of the implemented functions. The test results will be displayed, indicating whether each test has passed or failed.

## Conclusion

The FreeCodeCamp Forum Page Views Visualization project provides a comprehensive analysis of time series data using Python libraries such as Pandas, Matplotlib, and Seaborn. By running the project, you can explore the dataset, observe trends and growth in page views, and gain insights into the forum's popularity over time. The visualizations generated help in understanding the patterns and seasonality within the dataset, aiding in data-driven decision making and further analysis.

Note: Ensure that you have NumPy, Pandas, Matplotlib, and Seaborn installed on your system before running the project. 
