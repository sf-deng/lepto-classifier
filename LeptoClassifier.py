import pickle

import numpy as np
import pandas as pd

class LeptoClassifier():
    def __init__(self,):
        with open('data/svm_exclude_mat.pkl', 'rb') as f:
            self.svm_exclude_mat = pickle.load(f)
        with open('data/svm_include_mat.pkl', 'rb') as f:
            self.svm_include_mat = pickle.load(f)
        self.sd = pd.read_csv('data/sd.csv')
        self.prior = pd.read_csv('data/prior.csv')
            
    def predict(self, data_path, use_mat=False,):
        self.raw_data = pd.read_csv(data_path)
        self._sanity_check(use_mat)
        
        results = pd.Series([-1]*len(self.raw_data), index=self.raw_data.index)
        valid_rows = self.raw_data.notna().all(axis=1)
        self.raw_data.loc[valid_rows,'Prior'] = [self.prior[breed][0] for breed in self.raw_data[valid_rows]['Breed Group']]
        
        if use_mat:
            rows_with_zero_mat = (self.raw_data['MAT']==0) & (valid_rows)
            rows_with_low_mat = (self.raw_data['MAT']>0) & (self.raw_data['MAT']<=1600) & (valid_rows)
            rows_with_high_mat = (self.raw_data['MAT']>1600) & (valid_rows)
            
            # MAT = 0
            processed_data = self.raw_data[rows_with_zero_mat][self.sd.columns.drop('MAT')].div(self.sd.drop(columns=['MAT']).iloc[0])
            preds = self.svm_exclude_mat.predict(np.array(processed_data)) if len(processed_data)>0 else []
            results[rows_with_zero_mat] = preds
            
            # 0 < MAT <= 1600
            processed_data = self.raw_data[rows_with_low_mat][self.sd.columns]
            mat_to_log_mat = {
                100: 4,
                200: 5,
                400: 6,
                800: 7 ,
                1600: 8,
                }
            log_mat = [mat_to_log_mat[processed_data['MAT'].iloc[i]] for i in range(len(processed_data))]
            self.log_mat = log_mat
            processed_data['MAT'] = log_mat
            processed_data = processed_data.div(self.sd.iloc[1])
            self.processed_data = processed_data
            preds = self.svm_include_mat.predict(np.array(processed_data)) if len(processed_data)>0 else []
            results[rows_with_low_mat] = preds
            
            # MAT >= 3200
            results[rows_with_high_mat] = 1
        else:
            processed_data = self.raw_data[self.sd.columns.drop('MAT')].div(self.sd.drop(columns=['MAT']).iloc[0])
            preds = self.svm_exclude_mat.predict(np.array(processed_data)) if len(processed_data)>0 else []
            results[valid_rows] = preds
        
        return results
        
    def _sanity_check(self, use_mat):
        required_cols = set(self.sd.columns if use_mat else self.sd.columns.drop('MAT'))
        data_cols = set(self.raw_data.columns)
        missing_cols = required_cols-data_cols
        if missing_cols:
            raise ValueError(f'Data missing required column(s): {missing_cols}')
        
        
            