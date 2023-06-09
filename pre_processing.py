#importing libraries
import pandas as pd
import numpy as np
import os
import re

def make_dataset(path, exp_condition, exp_id):
    """
    Creates a dataset by importing and combining data from files that end with the specified experiment condition.
    
    Args:
        path (str): The path to the directory containing files to import.
        exp_condition (str): The suffix of the files to import. Only files that end with this suffix will be imported.
        exp_id (str): The ID of the experiment for which data is being imported. Can be 'exp_1' or 'exp_2'.
        
    Returns:
        pandas.DataFrame: The combined dataset with columns 'Experiment', 'part_id', 'sex', 'Condition', 'Sickness',
        and rows containing data from the imported files.
    """

    # Container to store the combined data
    dataset = pd.DataFrame(columns=range(6005))
    # Extracting only the desired files
    files = os.listdir(path)
    files = [os.path.join(path,f) for f in files if f.endswith(exp_condition)]

    for file,ind in zip(files, range(len(files))):
        #importing individual data
        if exp_id == 'exp_1':
            postural_data = pd.read_excel(file)

            #Extracting the sex of the participant
            #Returns all uppercase letters and extract the second element (sex)
            sex = re.findall(r"(?<=\d)[A-Za-z]", file)[0]
            #subsetting by direction of movement
            ML_data = pd.Series(postural_data.iloc[:, 1])
            AP_data = pd.Series(postural_data.iloc[:, 2])

        else:

            postural_data = pd.read_csv(file, header=None)
            sex = np.nan
            ML_data = pd.Series(postural_data.iloc[:, 0])
            AP_data = pd.Series(postural_data.iloc[:, 1])
        #Extracting participant ID
        participant_ID = re.findall(r'\d+(?=\D*$)', file)[0]

        #Assigning variables
        dataset.loc[ind, 0] = exp_id
        dataset.loc[ind, 1] = participant_ID
        dataset.loc[ind, 2] = sex
        dataset.loc[ind, 3] = exp_condition
        dataset.loc[ind, 4] = np.nan
        dataset.loc[ind, 5:3004] = ML_data.values
        dataset.loc[ind, 3005:] = AP_data.values

    #Renaming columns accordingly
    dataset = dataset.rename(columns={ 0: 'Experiment',1: 'part_id',2: 'sex',3: 'Condition',4:'Sickness'})
    return dataset

def add_sickness_status_from_ssq(dataset,dir):
    """
    This function adds sickness status from the SSQ (Symptom Severity Questionnaire) to the 
    dataset passed in as an argument. The function takes in two parameters:
    
    - `dataset` : A pandas DataFrame containing the data to which the SSQ sickness status is to be added.
    - `dir` : The directory from which the SSQ data is to be imported.
    
    The function first imports the necessary columns from the SSQ data and splits the participant ID 
    into `part_id` and `sex`. It then removes the unnecessary columns and renames the sickness column. 
    After that, it iterates over each row in the input dataset, extracts the participant ID and sex, 
    and adds the corresponding sickness status from the SSQ data to the dataset. Finally, it adds the 
    sickness status for participant 34M, who got sick on SSQ3. The output is the input dataset with 
    the sickness status added.
    """
    ssq_data = pd.read_excel(dir)
    #Importing only the necessary columns
    ssq_data = ssq_data.iloc[:, [0, 4]]

    #Splitting the participant ID into part_id and sex
    ssq_data['part_id'] = ssq_data.iloc[:,0].apply(lambda x: re.sub('[^0-9]', '', x))
    ssq_data['sex'] = ssq_data.iloc[:,0].apply(lambda x: re.findall('[A-Z]', str(x))[0])

    #Deleting unnecessary columns
    ssq_data = ssq_data.drop(columns=['Subject #'])

    #Renaming sickness column
    ssq_data = ssq_data.rename(columns={'Indicated they Were Sick on SSQ2?  (0=No,1=Yes)': 'Sickness'})

    #Adding sickness status
    for ind, row in dataset.iterrows():
        part_id = row['part_id']
        sex = row['sex']

        dataset.loc[ind, 'Sickness'] = ssq_data.loc[(ssq_data['part_id'] == part_id) & (ssq_data['sex'] == sex), 'Sickness'].values[0]

    #Adding the sickness status for participant 34M, who got sick on SSQ3
    dataset.loc[(dataset['part_id'] == '34') & (dataset['sex'] == 'M'), 'Sickness'] = '1'
    return dataset

def remove_rows_based_on_condition(dataset: pd.DataFrame, reference_dataset: pd.DataFrame) -> pd.DataFrame:
    """
    Removes rows from a dataset based on a condition specified in a reference dataset.

    Args:
        dataset: A pandas DataFrame containing the data to be filtered.
        reference_dataset: A pandas DataFrame containing the reference data to be used for filtering.

    Returns:
        A pandas DataFrame with the filtered data.
    """

    # Import only the necessary columns from the reference dataset
    reference_dataset = reference_dataset.iloc[:, [0, 2]]

    # Create a new DataFrame to avoid SettingWithCopyWarning
    new_reference = reference_dataset.copy()

    # Extract the part_id and sex from the 'Subject #' column
    new_reference.loc[:, 'part_id'] = reference_dataset.loc[:, 'Subject #'].apply(lambda x: re.findall('\d+', x)[0])
    new_reference.loc[:, 'sex'] = reference_dataset.loc[:, 'Subject #'].apply(lambda x: re.findall('[A-Z]', x)[0])

    # Iterate through each row in the dataset and remove it if it meets the condition
    for ind, row in dataset.iterrows():
        part_id = row['part_id']
        sex = row['sex']

        if new_reference.loc[(new_reference['part_id'] == part_id) & (new_reference['sex'] == sex), 'Driving Status'].item() == 'Passenger':
            dataset.drop(ind, inplace=True)

    return dataset

def retrieve_sex_and_cybersickness(dataset, reference_dataset,exp_id):
        
    '''
    Retrieves sex and cybersickness data from a dataset based on a reference dataset.

    :param dataset: A pandas dataframe containing the dataset to retrieve the sex and cybersickness data from.
    :type dataset: pandas.DataFrame
    :param reference_dataset: A pandas dataframe containing the reference dataset to use for retrieving sex and cybersickness data.
    :type reference_dataset: pandas.DataFrame
    :param exp_id: An experiment ID string to determine which columns to use for the reference dataset.
    :type exp_id: str

    :return: A pandas dataframe containing the retrieved sex and cybersickness data.
    :rtype: pandas.DataFrame
    '''

    #Importing only the necessary columns
    if exp_id == 'exp_2':
        reference_dataset = reference_dataset.iloc[:, [0, 2,8]]
    else:
        reference_dataset = reference_dataset.iloc[:, [0, 2,9]]

    #imputing sex and sickness
    for ind, row in dataset.iterrows():
            dataset.loc[ind, 'sex'] = reference_dataset.loc[reference_dataset['Participant'] == int(row['part_id']), 'Sex'].values[0]

            if reference_dataset.loc[reference_dataset['Participant'] == int(row['part_id']), 'Motion Sick? 2'].values[0] == 'Yes':
                    dataset.loc[ind, 'Sickness'] = '1'
            else:
                    dataset.loc[ind, 'Sickness'] = '0'

    return dataset



# Making datasets for experiment 1
# Importing data
path_exp1 = "data/exp_1/APAL 2019 Force Plate Data"
exp1_inspec = make_dataset(path_exp1, 'Inspection_Task.xlsx','exp_1')
exp1_search = make_dataset(path_exp1, 'Search_Task.xlsx','exp_1')

exp1_inspec = add_sickness_status_from_ssq(exp1_inspec, 'data/exp_1/APAL 2019 SSQ Data.xlsx')
exp1_search = add_sickness_status_from_ssq(exp1_search, 'data/exp_1/APAL 2019 SSQ Data.xlsx')

# Importing demographics data
demo_data_exp_1 = pd.read_excel('data/exp_1/APAL 2019_Cybersickness_Demographics_Data_v2.xlsx')

# Including only the participants who drove
exp1_inspec = remove_rows_based_on_condition(exp1_inspec, demo_data_exp_1)
exp1_search = remove_rows_based_on_condition(exp1_search, demo_data_exp_1)


# Making datasets for experiment 2
path_exp2 = "data/exp_2/force plate data"

exp2_inspec = make_dataset(path_exp2, 'inspection.txt', 'exp_2')
exp2_search = make_dataset(path_exp2, 'search.txt', 'exp_2')

#Importing demographics data
demo_data_exp2 = pd.read_excel('data/exp_2/Experiment 1 Demographics_Condition.xlsx')

exp2_inspec = retrieve_sex_and_cybersickness(exp2_inspec, demo_data_exp2,'exp_2')
exp2_search = retrieve_sex_and_cybersickness(exp2_search, demo_data_exp2,'exp_2')

# Making datasets for experiment 3
path_exp3 = "data/exp_3/force plate data"
exp3_inspec = make_dataset(path_exp3, 'inspection.txt', 'exp_3')
exp3_search = make_dataset(path_exp3, 'search.txt', 'exp_3')
demo_data_exp3 = pd.read_excel('data/exp_3/Experiment 2 Demographics_Condition.xlsx')
exp3_inspec = retrieve_sex_and_cybersickness(exp3_inspec, demo_data_exp3,'exp_3')
exp3_search = retrieve_sex_and_cybersickness(exp3_search, demo_data_exp3,'exp_3')

#Concatening datasets
inspection_df = pd.concat([exp1_inspec, exp2_inspec, exp3_inspec])
search_df = pd.concat([exp1_search, exp2_search, exp3_search])

#Exporting datasets
inspection_df.to_csv('data/inspection.csv', index=False)
search_df.to_csv('data/search.csv', index=False)




