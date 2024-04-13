import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError('List must contain nine numbers')
    matrix = np.array([list[:3],
                    list[3:6],
                    list[6:]])

    #calculating max and min values in each row
    max = []
    min = []

    for row in matrix:
        max.append(row.max())
        min.append(row.min())

    # finding the row with the maximum overall value and max value of the matrix
    row_sums = matrix.sum(axis=1)
    max_row_index = np.argmax(row_sums)
    max_row = matrix[max_row_index]
    max_row_value = max_row.max()

    # finding the row with the minimum overall value and min value of the matrix
    min_row_index = np.argmin(row_sums)
    min_row = matrix[min_row_index]
    min_row_value = min_row.min()

    # calculating sum
    sum_columns = matrix.sum(axis=0).tolist()
    sum_rows = matrix.sum(axis=1).tolist()
    sum_of_all_matrix = matrix.sum()

    # calculating mean
    mean_columns = matrix.mean(axis=0).tolist()
    mean_rows = matrix.mean(axis=1).tolist()
    mean_of_all_matrix = matrix.mean()

    # calculating variance

    variance_column = matrix.var(axis=0).tolist()
    variance_row = matrix.var(axis=1).tolist()
    flattened_variance = matrix.var()

    # calculating standard deviation

    std_column = matrix.std(axis=0).tolist()
    std_row = matrix.std(axis=1).tolist()
    flattened_std = matrix.std()




    return {
        'standard deviation': [std_column, std_row, flattened_std],
        'variance': [variance_column, variance_row, flattened_variance],
        'mean': [mean_columns, mean_rows, mean_of_all_matrix],
        'max': [max_row.tolist(), max, max_row_value],
        'min': [min_row.tolist(), min, min_row_value],
        'sum': [sum_columns, sum_rows, sum_of_all_matrix]
    }







    

result = calculate([2,6,2,8,4,0,1,5,7])
