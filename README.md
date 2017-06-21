# Udacity

Lesson 1 - Reading and Plotting Stock Data

Lesson outline
In this lesson you will learn how to read data, select subsets of it and generate useful plots, using pandas and matplotlib. The documentation links below are for your reference.

- Read stock data from CSV files:
- pandas.DataFrame
- pandas.read_csv
- Select desired rows and columns:
- Indexing and Slicing Data
- Gotchas: Label-based slicing conventions
- Visualize data by generating plots:
- Plotting
- pandas.DataFrame.plot
- matplotlib.pyplot.plot

Couple of points from Lesson one:

1) Real stock data looks like this:
Date, Open, High, Low, Close, Volume, Adj Close
(note this is for one particular stock, let us say Google. We need to have or represent this
data for all the stocks, so are we looking for something like a 3D view here??)

2) Currently each stock has its own .csv file that we can read and put in a data frame.


Lesson 2 - Working with multiple stocks

Lesson summary

To read multiple stocks into a single dataframe, you need to:
- Specify a set of dates using pandas.date_range
- Create an empty dataframe with dates as index
- This helps align stock data and orders it by trading date
- Read in a reference stock (here SPY) and drop non-trading days using pandas.DataFrame.dropna
- Incrementally join dataframes using pandas.DataFrame.join
- Once you have multiple stocks, you can:
- Select a subset of stocks by ticker symbols
- Slice by row (dates) and column (symbols)
- Plot multiple stocks at once (still using pandas.DataFrame.plot)
- Carry out arithmetic operations across stocks, e.g. normalize by the first day's price
