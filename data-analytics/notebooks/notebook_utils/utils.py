import pandas as pd
import numpy as np
import scipy.stats as stats
from scipy.stats import normaltest
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_context('paper', font_scale=2.0)

def healthy_sick_aggregated_info(
        individuals_info: pd.DataFrame,
        connections_info: pd.DataFrame) -> pd.DataFrame:
    """
    This function aggregates the information about healthy and sick people

    :param individuals_info: individual informations
    :param connections_info: informations about the relation between a sick an healthy connected people
    :returns pd.DataFrame with aggregated information for both sick and healthy connected people
    """
    # merging info about healthy people
    merge_healthy = pd.merge(
        right=connections_info,
        left=individuals_info.rename(
            columns={
                'name': 'V2'}),
        on='V2')

    # Renaming columns to distinguish information about healthy people
    cols_to_rename = [col for col in merge_healthy.columns.tolist() if col not in [
        'V1', 'V2', 'prob_V1_V2', 'grau', 'proximidade']]  # getting relevant columns for renaming
    cols_to_rename_dic = {col: col + '_healthy' for col in cols_to_rename}
    merge_healthy.rename(columns=cols_to_rename_dic, inplace=True)

    # merging info about sick people
    merge_sick = pd.merge(right=merge_healthy, left=individuals_info.rename(
        columns={'name': 'V1'}), on='V1')
    
    # Renaming columns to be more clear about sick people
    cols_healthy = [col for col in merge_healthy.columns.tolist()
                    if '_healthy' in col]
    cols_to_rename = [col for col in merge_sick.columns.tolist() if col not in [
        'V1', 'V2', 'prob_V1_V2', 'grau', 'proximidade'] + cols_healthy]  # getting relevant columns for renaming
    cols_to_rename_dic = {col: col + '_sick' for col in cols_to_rename}
    merge_sick.rename(columns=cols_to_rename_dic, inplace=True)

    # reordering columns
    cols_sick = [col for col in merge_sick.columns.tolist() if '_sick' in col]
    aggregated_info_df = merge_sick[['V1', 'V2', 'grau', 'proximidade'] +
                                    cols_healthy + cols_sick + ['prob_V1_V2']]

    return aggregated_info_df


def imc_class(imc: float) -> str:
    """
    This function classifies the Body Mass Index (BMI) into the levels according the World Health Organization
    """
    if imc <= 16.9:
        return 'muito_abaixo_peso'

    elif 17 <= imc <= 18.4:
        return 'abaixo_do_peso'

    elif 18.5 <= imc <= 24.9:
        return 'peso_normal'

    elif 25 <= imc <= 29.9:
        return 'acima_do_peso'

    elif 30 <= imc <= 34.9:
        return 'obesidade_lvl_1'

    elif 35 <= imc <= 40:
        return 'obesidade_lvl_2'

    elif imc > 40:
        return 'obesidade_lvl_3'

def d_agostino_k_2_test(data: np.array) -> float:
    """
    This function checks the gaussianity of data via D'Agostino's K-squared test. The p-value (p) is used to interpret the test, 
    in this case whether the sample was drawn from a Gaussian distribution.
    Hence, 

    p <= 0.05: reject H0, not normal
    p > 0.05: fail to reject H0, normal.
    """
    stat, p = normaltest(data)

    return p

class KruskallWallisTest:
    
    def __init__(self, data_frame: pd.DataFrame, categorical_var:str, continuous_var:str,categorical_values:list):

        """
        This class does the Kruskall Wallis (KW) test ad plot box charts for visual comparison between categorical variables and the numerical one.

        :param data_frame: data frame containing the data that we want apply the KW test
        :param categorical_var: categorical variable
        :param continuous_var: the numerical variable of interest
        :param categorical_value: list of all possible values for categorical variable
        """
        
        self.data_frame = data_frame
        self.categorical_var = categorical_var
        self.continuous_var = continuous_var
        self.categorical_values = categorical_values
        
        
    def get_p_value(self) -> float:
        """
        This method does the KW test and return the p-value.
        """
        arr = []
        for category in self.categorical_values:
            tmp = self.data_frame[self.data_frame[self.categorical_var]==category][[self.continuous_var]]
            tmp = tmp[~tmp['prob_V1_V2'].isnull()]
            arr.append(tmp)

        arr = np.array(arr,dtype=object)    
        return stats.kruskal(*arr).pvalue
    
    
    def box_plot(self, figsize:tuple, title:str):
        """
        This method plots box charts showing the ditribution of the numerical variable varying the categorical possible values. it useful for visual comparison
        and helps to see the KW test results.
        """
        box_data = self.data_frame.copy()
        box_data = box_data[~box_data[self.categorical_var].isnull()]
        plt.figure(figsize=figsize)
        sns.boxplot(x=self.categorical_var, y=self.continuous_var, data=box_data,showfliers = False)
        plt.title(title)
        plt.xticks(rotation=45)
        plt.show()


