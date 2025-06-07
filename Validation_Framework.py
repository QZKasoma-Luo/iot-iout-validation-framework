import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class DDoSValidationFramework:
    def __init__(self, data_set_name, data_set_path):
        self.data_set_name = data_set_name
        self.data_set_path = data_set_path
        self.df = None
        self.validation_results = {}

    def load_data(self):
        try:
            self.df = pd.read_csv(self.data_set_path)
            print(f"Data loaded successfully from {self.data_set_path}")
            return True
        except Exception as e:
            print(f"Error loading data: {e}")
            return False
        
    def validate_completeness(self):
        
        # Check for missing values in the dataset
        missing_stats ={
            'missing_all_rows': len(self.df),
            'missing_values': self.df.isnull().sum(),
            'missing_percentage': (self.df.isnull().sum() / len(self.df)) * 100
        }
        
        # check duplicates
        duplicate_rows = self.df.duplicated().sum()
        
        #check uniqueness of labels
        expected_types = {
            'Flow ID': 'object',
            'Src IP': 'object',
            'Dst IP': 'object',
            'Protocol': 'int64',
            'Flow Duration': 'int64',
            'Tot Fwd Pkts': 'int64',
            'Tot Bwd Pkts': 'int64',
            'Label': 'object'
        }