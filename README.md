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

Lesson outline
Here's an overview of what you'll learn to do in this lesson. Documentation links are for reference.

Read in multiple stocks:
  - Create an empty pandas.DataFrame with dates as index: pandas.date_range
  - Drop missing date rows: pandas.DataFrame.dropna
  - Incrementally join data for each stock: pandas.DataFrame.join

Manipulate stock data:
  - Index and select data by row (dates) and column (symbols)
  - Plot multiple stocks at once (still using pandas.DataFrame.plot)
  - Carry out arithmetic operations across stocks


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
  
  
Lesson 3


let us say we have a dataframe df1, which contains dates only. and We have another dataframe
for say google, now we need to make sure that we align the dates properly so that we map
and check correct dates.

"Joining" Dataframes

- pandas support join operations between two dataframes, the same way it is supported
in databases. We can even apply inner join etc.

- we first join empty data frames containing dates only with say the data frame containing
GOOGL data, then we join the result with say the data frame containing apple's information.
(Question  - why do we need to do it step by step)
(Question- are we creating separate data frames for each thing? like separate for high prices
separate for low prices etc)



Further things to check

- Date ranges
- multiple stocks
- align dates
- proper date order
- pandas support join operations that can be used between an empty df and another df
to pull data from the frame and populate empty data frame. So basically whenever we need to
customize our viewing of frames for any operations, think about joins.
- date_range() method. Pass start_date and end_date
- while creating an empty data frame, we can pass the index that we are working with. We
can say like df1 = pd.DataFrame(index=dates). If we do not provide this, then by default the
index will be 0,1,2 etc etc. So basically we can use this method to customize what kind of
indexes we want here.
- check for DateTimeIndex object

- join should happen between the known indexes else we will not see any data. If the index
of the two frames we are joining are different, then we need to tell pandas what index
we want to use for joining.

- we need to tell this to the df we are using on the right side, so that it matches the
df use din the left side.

- dropna() drops all the rows which has NaN values
- joins in pandas can be like inner join outer join etc, so check the need and use appropriate
parameter in "how" clause.


Slicing dataframes

- basically the way we can do slicing in python, we can do slicing in data frames as well
and we should do it as often as we want.

-  df2 = df1[start_date:end_date, ['GOOGL, 'GLD'']]

this statement will be used to filter data from start to end date for GOOGL and GLD only.
This is whenever we need to filter data try to put these kind of queries.

TODO - what kind of performance implications are there when we filter out the data???
TODO - when we keep on aliasing data frames does it just stores the markers to filtered data
or it actually stores the filtered data at a new location???

- categories of slicing
    - rowwise df.ix() function
        - dates need to be in chronological order else it will not work
        - df.ix[start:end]
        - ix function is not mandatory here
        - ix is pythonic
    - columnwise slicng
        df['GOOGL']
        df[['IBM', 'GOOGL']]
    - using both rowwise and columnwise
        df1[start_date:end_date, ['GOOGL, 'GLD'']]
        
Plotting the data

- we can use plot() function and we can try to make every stock start with same initial point
for a better look and feel and the comparison.

- how to normalize prize data so that everything starts from the same level??
- we are normalizing everything with respect to the first row
(see that it is very imp to understand normalization here)


there are two ways to do this;

for date in df1.index:
    for s in symbols:
        df1[date, s] = df1[date,s]/df1[date,0]
        
Or we can just do:

df1 = df1/df1[0] - this is faster as this is executed at low level using C

Quiz: How To Plot On "Equal Footing"?
Note: As per pandas syntax, the second option should actually read:
df = df / df.ix[0]

Or, to be more explicit:
df = df / df.ix[0, :]



Lesson summary

To read multiple stocks into a single dataframe, you need to:

- Specify a set of dates using pandas.date_range
- Create an empty dataframe with dates as index
  - This helps align stock data and orders it by trading date
- Read in a reference stock (here SPY) and drop non-trading days using pandas.DataFrame.dropna
- Incrementally join dataframes using pandas.DataFrame.join

Once you have multiple stocks, you can:

- Select a subset of stocks by ticker symbols
- Slice by row (dates) and column (symbols)
- Plot multiple stocks at once (still using pandas.DataFrame.plot)
- Carry out arithmetic operations across stocks, e.g. normalize by the first day's price

