import numpy as np
import pandas as pd
from scipy.stats import f_oneway
import statsmodels.api as sm
from statsmodels.formula.api import ols

def one_way_anova(data, groups, response):
    
    grouped_data = [group[response].values for _, group in data.groupby(groups)]
    f_stat, p_value = f_oneway(*grouped_data)
    print("\nOne-way ANOVA Results:")
    print(f"F-statistic: {f_stat:.4f}, p-value: {p_value:.4f}")
    if p_value < 0.05:
        print("Reject the null hypothesis: Significant difference among group means.")
    else:
        print("Fail to reject the null hypothesis: No significant difference among group means.")

def two_way_anova(data, response, factor1, factor2):
 
    formula = f"{response} ~ C({factor1}) + C({factor2}) + C({factor1}):C({factor2})"
    model = ols(formula, data).fit()
    print(sm.stats.anova_lm(model, typ=2))
    print("\nTwo-way ANOVA Results:")

if __name__ == "__main__":
    
    data_one_way = pd.DataFrame({
        "Group": np.repeat(['A', 'B', 'C'], 10),
        "Score": np.concatenate([
            np.random.normal(loc=50, scale=5, size=10),
            np.random.normal(loc=55, scale=5, size=10),
            np.random.normal(loc=60, scale=5, size=10)
        ])
    })

    one_way_anova(data_one_way, groups="Group", response="Score")

    data_two_way = pd.DataFrame({
        "Factor1": np.repeat(['Low', 'Medium', 'High'], 6),
        "Factor2": np.tile(['Type1', 'Type2'], 9),
        "Response": np.concatenate([
            np.random.normal(loc=50, scale=5, size=6),
            np.random.normal(loc=55, scale=5, size=6),
            np.random.normal(loc=60, scale=5, size=6)
        ])
    })

    two_way_anova(data_two_way, response="Response", factor1="Factor1", factor2="Factor2")