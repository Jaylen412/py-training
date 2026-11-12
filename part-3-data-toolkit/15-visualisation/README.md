# Module 15: Visualisation

Turn numbers into pictures. You will build charts with Matplotlib, choose the right chart for each question, combine and style plots so they make a point, and use seaborn for fast statistical graphics straight from DataFrames.

**Prerequisites:** Parts 1 and 2, and Modules 13 to 14.

Each lesson's `examples.py` saves its charts into a `figures/` folder next to the lesson, and `lesson.md` displays them.

## Lessons

1. [15-01 Matplotlib fundamentals](15-01-matplotlib-fundamentals/lesson.md)
2. [15-02 Chart types and when to use them](15-02-chart-types/lesson.md)
3. [15-03 Subplots and styling](15-03-subplots-and-styling/lesson.md)
4. [15-04 Statistical plots with seaborn](15-04-statistical-plots-with-seaborn/lesson.md)

## Checkpoint quiz

1. What is the difference between a figure and an axes?
2. Which chart would you use to show (a) how monthly revenue changed over a year, (b) the spread of house prices, (c) whether taller people weigh more?
3. Why should bar charts start at zero, and when should small multiples share an axis?
4. What does `hue="cultivar"` do in a seaborn plot?
5. A correlation heatmap shows −0.85 between two features. What does that mean?

<details>
<summary>Answers</summary>

1. The figure is the whole image; an axes is one plot inside it, with its own x and y axes. A figure can contain several axes.
2. (a) a line chart, (b) a histogram (or a box plot to compare groups), (c) a scatter plot.
3. Readers compare bar lengths, so cutting the axis exaggerates differences. Share axes when readers should compare sizes across panels.
4. It splits the data by the `cultivar` column, drawing each group in its own colour with a legend.
5. A strong negative relationship: when one feature is high, the other tends to be low.

</details>
