FTA_factors = ['2.3.1', '2.3.2', '2.3.3', '2.3.4', '2.3.5', '2.3.6', '2.3.7', '2.3.8',
              '3.8', '5.2', '4.1', '4.2', '4.4', '3.6', '5.3', '5.4', '3.3', '3.4',
              '3.5', '3.7', '3.9', '4.3', '4.5', '5.5']

for index, row in df_p.iterrows():
    count = sum(row[factor] > threshold for factor in risk_factors if factor not in FTA_factors)
    df_p.loc[index, 'p_ransomware_criteria'] = round(count/(len(risk_factors)-len(FTA_factors)),3)

FTA_factors = ['2.2.1', '2.2.2', '2.2.3', '2.2.4', '2.2.5', '2.2.6', '2.2.7', '2.2.8',
              '2.3.1', '2.3.2', '2.3.3', '2.3.4', '2.3.5', '2.3.6', '2.3.7', '2.3.8',
              '2.4', '3.8', '5.2', '1.7', '5.1', '1.3', '3.6', '5.3', '5.4', '3.3',
              '3.4', '3.5', '3.7', '3.9', '4.3', '4.5', '5.5']

for index, row in df_p.iterrows():
    count = sum(row[factor] > threshold for factor in risk_factors if factor not in FTA_factors)
    df_p.loc[index, 'p_phishing_criteria'] = round(count/(len(risk_factors)-len(FTA_factors)),3)

FTA_factors = ['2.2.1', '2.2.2', '2.2.3', '2.2.4', '2.2.5', '2.2.6', '2.2.7', '2.2.8',
              '2.3.1', '2.3.2', '2.3.3', '2.3.4', '2.3.5', '2.3.6', '2.3.7', '2.3.8',
              "5.7", "5.6", "1.5", "5.5", "3.8", "5.2", "2.4", "1.7", "5.1", "4.4", "4.2",
               "4.1", "4.5", "4.3", "3.9", "3.7", "3.5", "3.4", "3.3", "1.3", "3.6", "5.3", "5.4"]

for index, row in df_p.iterrows():
    count = sum(row[factor] > threshold for factor in risk_factors if factor not in FTA_factors)
    df_p.loc[index, 'p_insider_criteria'] = round(count/(len(risk_factors)-len(FTA_factors)),3)

FTA_factors = [
              '2.3.1', '2.3.2', '2.3.3', '2.3.4', '2.3.5', '2.3.6', '2.3.7', '2.3.8',
              "3.8", "5.2", "5.5", "2.4", "1.7", "5.1", "4.1", "4.4", "1.3", "3.6", "5.3",
               "5.4", "3.3", "3.4", "3.5", "3.7", "3.9", "4.3", "4.5"]

for index, row in df_p.iterrows():
    count = sum(row[factor] > threshold for factor in risk_factors if factor not in FTA_factors)
    df_p.loc[index, 'p_data_criteria'] = round(count/(len(risk_factors)-len(FTA_factors)),3)

FTA_factors = ['2.3.1', '2.3.2', '2.3.3', '2.3.4', '2.3.5', '2.3.6', '2.3.7', '2.3.8',
              "3.8", "5.2", "5.1", "5.5", "4.2", "1.3", "3.6", "5.3", "5.4", "3.3",
               "3.4", "3.5", "3.7", "3.9", "4.3", "4.5"]

for index, row in df_p.iterrows():
    count = sum(row[factor] > threshold for factor in risk_factors if factor not in FTA_factors)
    df_p.loc[index, 'p_supply_criteria'] = round(count/(len(risk_factors)-len(FTA_factors)),3)