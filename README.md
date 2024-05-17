# IGLY (Iel Gonna Let You)

## Description

Igly is an application designed to help you determine whether to continue in a relationship or not before it causes you harm. It utilizes machine learning and artificial intelligence techniques, primarily based on sociological studies concerning the reasons for divorce among married couples.

## Models

The models used in Igly are:

1. **KNN (K-Nearest Neighbors)**: A frequentist model that determines which individual in the model your situation corresponds to the most.
2. **Bayesian Model**: This model returns the likelihood of a breakup based on the study (database).

### Note:

For accuracy and relevance, the data has been amplified, adhering to the statistics of the conducted study. This was achieved using the following Python algorithm:

```python
import pandas as pd
import numpy as np

def simulate_data(csv_file_path, num_simulated_rows):
    """
    Simulates fictitious data based on an existing CSV file.

    Parameters:
    - csv_file_path: Path to the original CSV file.
    - num_simulated_rows: Number of rows of simulated data to generate.

    Returns:
    - DataFrame containing the simulated data.
    """

    # Read the original data
    df = pd.read_csv(csv_file_path, delimiter=';')

    # DataFrame for the simulated data
    simulated_data = pd.DataFrame()

    # For each column in the original DataFrame
    for column in df.columns:
        if df[column].dtype == np.number:
            # For numerical columns, simulate data based on a normal distribution
            mean = df[column].mean()
            std = df[column].std()
            simulated_data[column] = np.random.normal(loc=mean, scale=std, size=num_simulated_rows)
        else:
            # For non-numerical columns, randomly choose existing values
            simulated_data[column] = np.random.choice(df[column], size=num_simulated_rows)
    
    return simulated_data
```

Igly aims to leverage these advanced techniques to provide you with insights into the viability of your relationship, helping you make informed decisions based on data-driven analysis.

## Original Dataset
- Dr. Mustafa Kemal Yöntem, Nevşehir Hacı Bektaş Veli University, Faculty of Education, Department of Educational Sciences, muskemtem '@' hotmail.com
- Dr. Kemal ADEM, Aksaray University, Faculty of Economics and Administrative Sciences, Department of Management Information Systems, kemaladem '@' gmail.com
- Prof. Dr. Tahsin İlhan, Tokat GAZİOSMANPAŞA University, Faculty of Education, Department of Educational Sciences, tahsinilhan73 '@' gmail.com
- Lecturer Serhat Kılıçarslan, Tokat GAZİOSMANPAŞA University, Rectorate, Department of Informatics, serhatklc '@' gmail.com

### References
>- M. K. Yöntem et al. (2019). Divorce Prediction Using Correlation Based Feature Selection and Artificial Neural Networks.
>- Dua, D. and Graff, C. (2019). UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science.
>- T. A. DeWees et al. (2020). Investigation Into the Effects of Using Normal Distribution Theory Methodology for Likert Scale Patient-Reported Outcome Data From Varying Underlying Distributions Including Floor/Ceiling Effect.