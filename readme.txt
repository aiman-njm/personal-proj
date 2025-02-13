Data Cleaning Process
Objective:
The dataset originally contained 1,000 rows of YouTube's most popular videos, with attributes such as views, likes, dislikes, category, and published year. However, the raw data had inconsistencies that required cleaning before analysis.

Steps Taken to Clean the Data:

Converted Text-Based Numbers to Numeric Values:

Columns "Video views," "Likes," and "Dislikes" were originally stored as text with commas (e.g., 54,071,677).
Removed commas and converted them into numerical format to allow calculations.
Handled Missing Values:

The "Dislikes" column had missing values. Since YouTube removed public dislikes, missing values were replaced with 0 to indicate unavailable data.
The "Category" column had some missing values, which were replaced with "Unknown" to ensure all rows had a category.
Standardized Data Types:

Ensured numerical columns were stored as appropriate numeric types (float or int).
Kept the "published" column as an integer representing the year.
Why This Was Done:

This cleaning process ensures accurate calculations, meaningful visualizations, and better trend analysis in the project.
