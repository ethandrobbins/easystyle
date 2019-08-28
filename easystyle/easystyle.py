import pandas as pd
import numpy as np
import seaborn as sns

class style(object):
    #Functions to highlight negative cells
    def fake_highlight_negative(val, color):
        if val < 0:
            colorDum = color
        else:
            colorDum = ''
        return 'color: %s' % colorDum

    def highlight_negative(df, col = 'red'):
        return df.style.applymap(fake_highlight_negative, color = col)


    #Functions to highlight positive cells
    def fake_highlight_positive(val, color):
        if val > 0:
            colorDum = color
        else:
            colorDum = ''
        return 'color: %s' % colorDum

    def highlight_positive(df, col = 'green'):
        return df.style.applymap(fake_highlight_positive, color = col)


    #Functions used to highlight positive and negative cells
    def fake_highlight_neg_pos(val, colorNeg, colorPos):
        if val > 0:
            colorDum = colorPos
        elif val < 0:
            colorDum = colorNeg
        else:
            colorDum = ''
        return 'color: %s' % colorDum

    def highlight_neg_pos(df, colNeg = 'red', colPos = 'green'):
        return df.style.applymap(fake_highlight_neg_pos, colorNeg = colNeg, colorPos = colPos)


    #Functions to highlight the maximum in column(s)
    def fake_highlight_max(col, color):
        is_max = col == col.max()
        return ['background-color: ' + color if v else '' for v in is_max]

    def highlight_max(df, column_names, col='yellow'):
        return df.style.apply(fake_highlight_max, color=col, subset=column_names)

    #Function to highlight the minimum in column(s)
    def fake_highlight_min(col, color):
        is_min = col == col.min()
        return ['background-color: ' + color if v else '' for v in is_min]

    def highlight_min(df, column_names, col='orange'):
        return df.style.apply(fake_highlight_min, color=col, subset=column_names)

    #Functions to highlight outliers
    def fake_highlight_outlier_lower(col, color):
        Q1 = col.quantile(0.25)
        Q3 = col.quantile(0.75)
        IQR = Q3 - Q1
        bottom = col < Q1 - 1.5 * IQR
        return ['background-color: ' + color if v else '' for v in bottom]

    def fake_highlight_outlier_upper(col, color):
        Q1 = col.quantile(0.25)
        Q3 = col.quantile(0.75)
        IQR = Q3 - Q1
        top = col > Q3 + 1.5 * IQR
        return ['background-color: ' + color if v else '' for v in top]

    def highlight_outlier(df, column_names, colLow='red', colUp='red'):
        return df.style.apply(fake_highlight_outlier_lower, color=colLow, subset=column_names).apply(fake_highlight_outlier_upper, color=colUp, subset=column_names)

    #Function to highlight NaN values
    def highlight_NaN(df, color = 'red'):
        return df.style.highlight_null(null_color=color)

    #Function to give gradient to the table
    def highlight_gradient(df, color = 'green'):
        pal = sns.light_palette(color, as_cmap = True)
        return df.style.background_gradient(cmap = pal)
