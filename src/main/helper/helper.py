import numbers
import re

import pandas as pd
import json
import numpy as np


def get_parameter_from_excel(sheet_name):
    test_data = []
    # get name of the first row
    keys = pd.read_excel(get_config("test_data_file"), sheet_name=sheet_name).keys().values
    # get all data of one sheet
    df = pd.read_excel(get_config("test_data_file"), sheet_name=sheet_name)
    # for loop create list of tuple for parameterize in pytest
    for i in range(0, len(df.iloc[:, 0])):
        temp = []
        get_value = df.iloc[i, :]
        for j in range(1, len(keys)):
            # because when the value is integer is will take some problems, so this function will convert int to str
            if isinstance(get_value[j], numbers.Integral):
                temp.append(str(get_value[j]))
            else:
                temp.append(get_value[j])
        # add tuple to list of tuples
        test_data.append(tuple(temp))

    # return type: {(tuple1), (tuple2), ...}
    # if excel contains only one test colum data should use * before keyword to get origin value
    return test_data


def get_data_from_excel(sheet_name):
    test_data = {}
    # get name of the first row
    keys = pd.read_excel(get_config("test_data_file"), sheet_name=sheet_name).keys().values.tolist()
    # get all data of one sheet
    df = pd.read_excel(get_config("test_data_file"), sheet_name=sheet_name)
    for i in range(len(keys)):
        # use map function to convert the value from in to str
        # string.tolist() mean separate each word in string to an element of list
        test_data[keys[i]] = list(map(str, df[keys[i]].values.tolist()))
    # return type object like {"key1": [list1], "key2": [list2], ...}
    return test_data


def get_data_frame_from_excel(sheet_name):
    test_data = {}
    # get name of the first row
    keys = pd.read_excel(get_config("test_data_file"), sheet_name=sheet_name).keys().values.tolist()
    # get all data of one sheet
    df = pd.read_excel(get_config("test_data_file"), sheet_name=sheet_name)
    for i in range(len(keys)):
        # use map function to convert the value from in to str
        # string.tolist() mean separate each word in string to an element of list
        test_data[keys[i]] = list(map(str, df[keys[i]].values.tolist()))
    # return a dataframe
    return pd.DataFrame(test_data)


def get_config(key):
    # get value by key in config.json file
    conf_file = open("config.json")
    data = json.load(conf_file, )
    conf_file.close()
    return data[key]


def compare_data_frame(df1, df2):
    # create a new numpy array
    rs = np.array([])
    for col in df1.head():
        # print(f"column: {col}")
        # compare value and data type of dataframe column with numpy
        check = np.where(df1[col].values == df2[col].values, "T", "F")
        # join numpy array
        rs = np.hstack((rs, check))

    if "F" in rs:
        return False
    else:
        return True


def check_string_in_data_frame(value, dataframe, direction):
    # Use pandas.DataFrame.shape to get the shape of the DataFrame,
    # which is a tuple where the first element is a number of rows and the second is the number of columns
    # get number of rows
    value = str(value)
    if direction == "row":
        result = np.array([])
        for i in range(dataframe.shape[0]):
            if len(dataframe.index) == 0:
                return None
            else:
                # check contains string with pandas series contains function ignore cases
                check = dataframe.iloc[i].str.contains(value)
                result = np.hstack((result, check))
        if 1 in result:
            return True
        else:
            return False
    elif direction == "column":
        result = np.array([])
        # check data in dataframe
        for i in dataframe.head():
            # if dataframe is empty return None
            if len(dataframe.index) == 0:
                return None
            else:
                # check contains string with pandas series contains function ignore cases
                # must
                check = dataframe[i].str.contains(value)
                # print(f"this check values: {value}")
                # print(f"check values {check}")
            result = np.hstack((result, check))
        if 1 in result:
            return True
        else:
            return False
