# easystyle

easystyle is a python package created to allow simple and quick data analysis without having to import to excel. easystyle reads in the data as a dataframe. The package is heavily dependent on the styling in pandas. The package pulls a lot of information from the Styling pandas documentation. Functions such as identifying, by highlighting the cell, the maximum, the minimum, outliers, NaN values are used in easystyle. These functions allow the user to take a quick look at their data in Jupyter Notebook. It also serves the purpose of showing the data cleaner than with a standard dataframe so that you can present the information to others without having to go to excel.


## Installing easystyle

    pip install easystyle

## Importing easystyle

The best way to import easy style is:

    from easystyle import Style as es
This is since it makes it simpler to call functions when using the package. For the following examples we will assume this importing method.

## Highlight Negative Values

    def highlight_negative(df, col = 'red'):
In order to use highlight_negative, the user must provide the dataframe. The user does not need to provide a color, but may do so if they want a color other than red. To run the function:

    df = es.highlight_negative(df, color)

## Highlight Positive Values

    def highlight_positive(df, col = 'green'):
This function follows similarly to the function above. To run the function:

    df = es.highlight_positive(df, color)


## Highlight Negative and Positive Values

    def highlight_neg_pos(df, colNeg = 'red', colPos = 'green'):
Follows from above. To run the function:

    df = es.highlight_neg_pos(df, color_neg, color_pos)

## Highlight Maximum Value

    def highlight_max(df, column_names, col='yellow'):
The function is feed an additional variable than before, the column names. `column_names` is an array of the column names that you wish to find the maximum in. For example:

    column_names = ['A', 'B', 'C']
    df = highlight_max(df, column_names, color)

## Highlight Minimum Value

    def highlight_min(df, column_names, col='orange'):
Follows similarly to highlighting a maximum value. For example:

    column_names = ['A', 'B', 'C']
    df = highlight_min(df, columns_names, color)

## Highlight Outliers

    def highlight_outlier(df, column_names, colLow='red', colUp='red'):
This function uses the IQR method in order to find outliers. Again, `column_names` is a array of column names. For example:

    df = highlight_outlier(df, column_names, colorLower, colorUpper)

## Highlight NaN Values

    def highlight_NaN(df, color = 'red'):
If any NaN values are detected, they are highlighted. For example:

    df = highlight_NaN(df, color)

## Give a Gradient

    def highlight_gradient(df, color = 'green'):
This function uses the gradients provided by the Seaborn package. For example:

    df = highlight_gradient(df, color)

