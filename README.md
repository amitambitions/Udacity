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


The power of Numpy

Lesson outline
If you're familiar with NumPy (esp. the following operations), feel free to skim through this lesson.

Create a NumPy array:
    - from a pandas dataframe: pandas.DataFrame.values
    - from a Python sequence: numpy.array
    - with constant initial values: numpy.ones, numpy.zeros
    - with random values: numpy.random
Access array attributes: shape, ndim, size, dtype
Compute statistics: sum, min, max, mean
Carry out arithmetic operations: add, subtract, multiply, divide
Measure execution time: time.time, profile
Manipulate array elements: Using simple indices and slices, integer arrays, boolean arrays

Some notes from the videos:

- Numpy is a wrapper to numerical libraries
- panda is a kind of wrapper to the Numpy, pandas creates sort of indexes and column names on
top of the ndarray elements present beneath
- let us say we have a dataframe where indexes are dates and the column names are the names of the 
companies holding those stocks. The actual values are nothing but ndarray (check whats ndarray)
and this can be fetched from the panda data frame using nd1 = df1.values

https://docs.scipy.org/doc/numpy-1.12.0/reference/arrays.ndarray.html

Notes on notations

- nd1[row, column]
- nd1[0:3, 1:4] - this can give us a subset of the whole 2d array. So since all these are built
on top of python, we can think of using slicing as often as we want.
- nd1[:, 1:4] - all rows
- we can use negative numbers as python slices supports that. We can start with -1 for the 
last row and carry from there.
- to copy elements from one ndarray to another we can use a simple assignment operation.
we can just say nd1[..] = nd1[...]
- we can convert various python operations to ndarray. Let us say we want to convert a list
to a 1D array, then we can simply do like
- we can access underlying values of the numpy array using.values() method


Creating an ndarray from scratch

np.array([1,2,,3])
- input can be anything which follows a sequence like a list, tuple etc

- for 2d array, just pass sequence of sequences
np.array([(1,2,3), (4,5,6)])

np.empty(5)
np.empty((5,5)) - check that we need to pass data in double parenthesis here because
it wil take the tuple to decide the dimension of the array to be created.
- note here that by default the values contained in this array will be junk values
- we can create default values using different functions

np.ones((5,4)) - this will create an array with all 1s
- default data type will always be floating points

np.ones((5,), dtype=np.int)
will give new datatypes.


- Below statement will generate an array full of random numbers, uniformly sampled from [0.0, 1.0)
- np.random.random((5,4))
- by default the numbers are samples from 0 to 1
- np.random.normal(size=(2,3))

Normal or gaussian distribution is also supported. Need to check how to do this
- default mean will be 0.0 and standard deviation will be 1.0
- we can ofcourse change it by providing that as a parameter np.random.normal(50,10, size=(2,3))

randint can be used to generate integers
- use size for array and rest we know

Array Attributes
    
a = np.random.random((5,4))
a.shape
this will give the tuple of the size of the array

a.shape[0] - return number of rows
a.shape[1] - return number of columns
len(a.shape) - this will give the dimension of the tuple

a.size - will give the total number of elements present
a.dtype will give the datatype
a.sum - sum of all elements
a.sum(axis=0) - sum of all rows
a.sum(axis=1) - sum of all columns
a.min(axis=0)
a.max(axis=1)
a.mean()



time.time() - to get the time and we can use this to get the time executed by soem python code

"""Numpy timing comparison."""

import numpy as np

def manual_mean(arr):
    sum = 0
    for i in xrange(0, arr.shape[0]):
        for j in xrange(0, arr.shape[1]):
            sum += arr[i,j]
    return sum/arr.size
    
def numpy_mean(arr):
    return arr.mean()
    
Numpy is super fast as compared to manual iteration. Why so? Seems like Numpy is a wrapper
on top of the C code and hence it is faster.


a[3,2] - to access elements. first is the row number, second is the column number
a[0, 1:3] - slicing
a[:, 0:3:2] - starts at first, stops before second and everytime takes a jump of the last
value, which is 2 here.
a[0,0] = 1
a[0,:] = 2
a[:,3] = [1,2,3,4,5]



indices = np.array([1,1,2,3])
print a[indices]

it will print all these indices
(this is like passing array of indices to another array)



a = np.array([(5,10....),(values here too)])
lets us say we want all values less that the mean

- calculate mean by a.mean()
- either run a loop, which will of course be more time consuming
- or use numPy and say print a[a < mean]
- we can also say

a[a < mean] = mean


Arithmetic Operations

- a = np.array[(), ()]
- 2 * a - will multiply every element by 2 (a new array is created, so need to be careful of what 
we want here to save some time)
- similarly division and addition will work
- a + b of two different arrays (shape should be similar)
- multi of two different arrays will do it elemnt wise and NOT based on how a matrix multiplication
happens
- dot() function can be used for matrix multiplication
