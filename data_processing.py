import unicodedata
import re
import os
import time

class DataProcessor:

    def __init__(self) -> None:
        self.ewe_dataset = "data/jw300.en-ee.en"
        self.english_dataset = "data/jw300.en-ee.ee"
        self.extra_dataset = "data/EWE_ENGLISH.csv"
        self.data_len = 1000

    def read_dataset(self, data_len=1000) -> list:
        '''
        This function read the same length of data from both language datasets and returns a list of both languages.
        It is set to default to 1000 lines but an optional argument can be passed to specify the number of lines to
        read. If the number of lines is greater than that of the dataset, it returns the maximum length of dataset 
        with a prompt,
        params: data_len (The desired length of list to return from both datasets)
        return:ewe_list, english_list
        '''
        self.data_len = data_len
        ewe_list = []
        english_list = []
        with open(self.ewe_dataset, 'r+b') as ewe, open(self.english_dataset, 'r+b') as english:

            ewe_lines = ewe.readlines()
            english_lines = english.readlines()
            max_len = min(len(ewe_lines), len(english_lines))
            if max_len<self.data_len:
                print(f"There are only {max_len} lines in dataset. Returning only {max_len} lines")
            for i in range(min(self.data_len, max_len)):
                ewe_list.append(ewe_lines[i].decode('utf-8').strip())
                english_list.append(english_lines[i].decode('utf-8').strip())
        
        return ewe_list, english_list
        