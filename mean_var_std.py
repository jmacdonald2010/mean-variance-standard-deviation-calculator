import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')
    input_array = np.array([[list[0], list[1], list[2]], [list[3], list[4], list[5]], [list[6], list[7], list[8]]])
    calculations = dict()
    print(input_array)

    # calc mean
    c_mean = np.mean(input_array, axis=0) # axis 0 is column
    r_mean = np.mean(input_array, axis=1)
    f_mean = np.mean(input_array)
    calculations['mean'] = [c_mean.tolist(), r_mean.tolist(), f_mean]

    # variance
    c_var = np.var(input_array, axis=0)
    r_var = np.var(input_array, axis=1)
    f_var = np.var(input_array)
    calculations['variance'] = [c_var.tolist(), r_var.tolist(), f_var]

    # standard dev
    c_std = np.std(input_array, axis=0)
    r_std = np.std(input_array, axis=1)
    f_std = np.std(input_array)
    calculations['standard deviation'] = [c_std.tolist(), r_std.tolist(), f_std]

    # max
    c_max = np.amax(input_array, axis=0)
    r_max = np.amax(input_array, axis=1)
    f_max = np.amax(input_array)
    calculations['max'] = [c_max.tolist(), r_max.tolist(), f_max]

    # min
    c_min = np.amin(input_array, axis=0)
    r_min = np.amin(input_array, axis=1)
    f_min = np.amin(input_array)
    calculations['min'] = [c_min.tolist(), r_min.tolist(), f_min]

    # sum
    c_sum = np.sum(input_array, axis=0)
    r_sum = np.sum(input_array, axis=1)
    f_sum = np.sum(input_array)
    calculations['sum'] = [c_sum.tolist(), r_sum.tolist(), f_sum]

    return calculations

# this code below is for testing the function, and what the dict should look like when outputting data
# test calculations
print(calculate([0,1,2,3,4,5,6,7,8]))
# should return:
'''
{
  'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0], 
  'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667], 
  'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
  'max': [[6, 7, 8], [2, 5, 8], 8],
  'min': [[0, 1, 2], [0, 3, 6], 0],
  'sum': [[9, 12, 15], [3, 12, 21], 36]
}'''