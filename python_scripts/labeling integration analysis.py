import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def plot_kde(df, fta_col, criteria_col, label_col, xlabel, colors, label_names):
    sns.set(style='white')
    plt.figure(figsize=(6, 3.5))
    
    # Plotting multiple datasets
    sns.kdeplot(df[fta_col], color=colors[0], fill=True, label=label_names[0], alpha=0.5)
    sns.kdeplot(df[criteria_col], color=colors[1], fill=True, label=label_names[1], alpha=0.5)
    sns.kdeplot(df[label_col], color=colors[2], fill=True, label=label_names[2], alpha=0.5)

    plt.xlabel(xlabel)
    plt.ylabel('Density')
    plt.xlim(0,1)
    if fta_col=='p_phishing_FTA' or fta_col=='p_data_FTA' : plt.legend(loc='upper left')
    else: plt.legend(loc='upper right')
    plt.show()

# Define earth tone colors
earth_colors = sns.color_palette('Set2', n_colors=3)
label_names = ['FTA', 'Criteria', 'Ensembled']

plot_kde(df_p, 'p_ransomware_FTA', 'p_ransomware_criteria', 'p_ransomware_label', 'Risk degrees of ransomware', earth_colors, label_names)
plot_kde(df_p, 'p_phishing_FTA', 'p_phishing_criteria', 'p_phishing_label', 'Risk degrees of phishing', earth_colors, label_names)
plot_kde(df_p, 'p_insider_FTA', 'p_insider_criteria', 'p_insider_label', 'Risk degrees of insider attack', earth_colors, label_names)
plot_kde(df_p, 'p_data_FTA', 'p_data_criteria', 'p_data_label', 'Risk degrees of data breach', earth_colors, label_names)
plot_kde(df_p, 'p_supply_FTA', 'p_supply_criteria', 'p_supply_label', 'Risk degrees of supply chain attack', earth_colors, label_names)
