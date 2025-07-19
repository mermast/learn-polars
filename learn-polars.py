import polars as pl

# check the version of polars and dependencies ----
pl.show_versions()

# chapter 2 --> polars configuration
# chapter 3 --> Relaxedness and comparisino to pandas
# chapter 4 --> null values in polars

coordinates = pl.DataFrame(
 [
 pl.Series("point_2d", [[1, 3], [2, 5]]),
 pl.Series("point_3d", [[1, 7, 3], [8, 1, 0]]),
 ],
 schema={
 "point_2d": pl.Array(shape=2, inner=pl.Int64),
 "point_3d": pl.Array(shape=3, inner=pl.Int64),
 },
)
coordinates


weather_readings = pl.DataFrame(
 {
 "temperature": [[72.5, 75.0, 77.3], [68.0, 70.2]],
 "wind_speed": [[15, 20], [10, 12, 14, 16]],
 }
)
weather_readings


# CONSTRUCT A POLARS SERIES ------------------------------------------------------------------------
# A Series represents a single column/row in a Polars DataFrame.

# pl.Series(name, values, dtype, strict = True)
pl.Series(name = "a", values = [1, 2, 3])
pl.Series("a", [1, 2, 3], dtype=pl.Float32)
pl.Series("a", [1, 2, 3], dtype=pl.UInt16)

# no relaxedness in polars
pl.Series("a", [1, 2, 3.12])
pl.Series("a", [1, 2, 3.12], dtype=pl.UInt16)
pl.Series("a", [1, 2, 3.12], dtype=pl.UInt16, strict= True)
pl.Series("a", [1, 2, 3.12], dtype=pl.UInt16, strict= False)

pl.Series('names', ['Jack','Alen','Phil','Douge'])
pl.Series('mask', [True, False, False])

# a series without name
pl.Series([True, False, False])

# ATTRIBUTES OF SERIES
s = pl.Series([True, False, False])
s.dtype
s.shape
s.name

s = pl.Series('mask', [True, False, False])
s.name


# CONSTRUCTION OF DATA FRAMES ------------------------------

# data frame from dict -- autoamticaly infer the datatype
pl.DataFrame({'name':['jack','alen'], 'age': [29,32]})

# data frame from dict -- specify data types
pl.DataFrame({'name':['jack','alen'], 'age': [29,32]},
            schema= {'name':pl.String, 'age' : pl.UInt16})

pl.DataFrame({'name':['jack','alen'], 'age': [29,32]},
            schema= [('name',pl.String), ('age',pl.UInt16)])

# data frame from series ---
data = [
    pl.Series("col1", [1, 2], dtype=pl.Float32),
    pl.Series("col2", [3, 4], dtype=pl.Int64),
]
pl.DataFrame(data)

# data frame from lists
data = [[1, 2, 3], [4, 5, 6]]
pl.DataFrame(data, schema=["a", "b", "c"], orient="row")
pl.DataFrame(data, schema=["a", "b"], orient="col")

# from csv files
df1 = pl.read_csv('/workspaces/learn-polars/data/all_stocks.csv')
df1.estimated_size('mb')

df2 = pl.read_csv('/workspaces/learn-polars/data/all_stocks.csv',
                 schema= {'symbol':pl.String,
                          'date':pl.Date,
                          'open':pl.Float32,
                          'high':pl.Float32,
                          'low':pl.Float32,
                          'close':pl.Float32,
                          'adj close':pl.Float32,
                          'volumn':pl.UInt32})
df2.estimated_size('mb')

df2.estimated_size('mb') / df1.estimated_size('mb')

df1.head()
df2.head()

df1.tail()
df2.tail()


# reading only first 3 rwos
pl.read_csv('/workspaces/learn-polars/data/all_stocks.csv', n_rows= 3)

# read from 100th onwards rows
pl.read_csv('/workspaces/learn-polars/data/all_stocks.csv', skip_rows= 100).write_csv('temp.csv')



pl.read_parquet('/workspaces/learn-polars/data/simul/sim_rtds_combined-1.parquet')





