import numpy as np
import pandas as pd
from scipy import stats

exam_scores = np.array([85, 87, 90, 78, 88, 95, 82, 79, 94, 91])

group_A = np.array([85, 89, 88, 90, 93, 85, 84, 79, 90, 87])
group_B = np.array([82, 86, 85, 87, 92, 80, 81, 78, 89, 85])

before_treatment = np.array([82, 84, 88, 78, 80, 85, 90, 79, 87, 83])
after_treatment = np.array([85, 87, 89, 81, 83, 88, 92, 82, 89, 86])

def one_sample_ttest(data):
    population_mean=np.mean(exam_scores)
    t_stat, p_value = stats.ttest_1samp(data, population_mean)
    print("One-Sample T-Test:")
    analyze_ttest_results(t_stat, p_value)

def two_sample_ttest(group1, group2):
    t_stat, p_value = stats.ttest_ind(group1, group2)
    print("Two-Sample T-Test:")
    analyze_ttest_results(t_stat, p_value)

def paired_sample_ttest(before, after):
    t_stat, p_value = stats.ttest_rel(before, after)
    print("Paired-Sample T-Test:")
    analyze_ttest_results(t_stat, p_value)

def analyze_ttest_results(t_stat, p_value, alpha=0.05):
    print(f"T-statistic: {t_stat}")
    print(f"P-value: {p_value}")
    if p_value < alpha:
        print("Result: The null hypothesis is rejected")
    else:
        print("Result: The null hypothesis is accepted")

one_sample_ttest(exam_scores)
two_sample_ttest(group_A, group_B)
paired_sample_ttest(before_treatment, after_treatment)