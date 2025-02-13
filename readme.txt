YouTube Data Visualization Dashboard
Project Overview:
This project analyzes the most popular YouTube videos dataset to uncover trends in video engagement, such as views, likes, and category distribution. The dataset was cleaned and processed before building an interactive dashboard using Python, Dash, and Plotly.

Data Cleaning Process
Objective:
The original dataset contained 1,000 rows of YouTube’s most popular videos with attributes such as video title, views, likes, dislikes, category, and published year. However, raw data inconsistencies required cleaning before performing analysis.

Steps Taken to Clean the Data:
1. Converted Text-Based Numbers to Numeric Values
The columns "Video views," "Likes," and "Dislikes" were originally stored as text with commas (e.g., 54,071,677).
Removed commas and converted them into numerical format to enable calculations.
2. Handled Missing Values
"Dislikes" Column: Since YouTube removed public dislikes, missing values were replaced with 0 to indicate unavailable data.
"Category" Column: Some videos had missing categories, which were replaced with "Unknown" to maintain consistency.
3. Standardized Data Types
Ensured numerical columns (views, likes, dislikes) were stored as appropriate numeric types (int or float).
Kept the "published" column as an integer year format for accurate time-based filtering.
Why This Was Done?
To ensure accurate calculations for meaningful visualizations.
To avoid errors in data aggregation and filtering.
To provide better insights into YouTube video trends.
Data Visualization Dashboard
The interactive dashboard was built using Dash and Plotly, allowing users to analyze YouTube trends dynamically. Users can filter data based on category and year, and upload new datasets for real-time analysis.

Key Features:
Top 10 Most Viewed Videos

Displays the 10 most viewed videos in the dataset.
Interactive bar chart with color-coded views.
Video Category Distribution

Pie chart showing the distribution of video categories.
Users can see which categories dominate the top trending videos.
Views and Likes Over Time

Trend line graph displaying total video views and likes over the years.
Helps to analyze engagement trends over time.
Likes vs. Views Correlation

Scatter plot to examine the relationship between likes and views.
Determines whether highly viewed videos also get more likes.
Total Statistics Summary

Displays key stats such as Total Views, Total Likes, and Most Popular Category.
Updates dynamically based on applied filters.
Interactivity:
✅ Filters: Users can filter data by category and year range.
✅ File Upload: Allows users to upload a new dataset, which dynamically updates the dashboard.
✅ Dark Theme UI: Uses Dash Bootstrap Components (CYBORG theme) for a sleek appearance.

Future Improvements
🔹 Add more visualizations (e.g., engagement by video length).
🔹 Enhance filtering (e.g., filter by video title keywords).
🔹 Implement machine learning to predict trending videos.

Conclusion
This project provides an interactive and real-time analysis of YouTube’s top videos, helping users visualize and understand video engagement trends. The data cleaning and visualization techniques ensure a high-quality dataset for accurate insights.

