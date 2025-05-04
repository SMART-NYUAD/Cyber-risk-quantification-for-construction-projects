# risk 1
from IPython import get_ipython
# This gets the 'interactive shell' object, which represents the running IPython instance.
shell = get_ipython()
# Now you can access variables in the shell's namespace:
df_p = shell.user_ns['df_p']

for i in df_p.index:

    p6 = max(df_p.loc[i, '2.3.1'], df_p.loc[i, '2.3.2'], df_p.loc[i, '2.3.3'], df_p.loc[i, '2.3.4'],
                 df_p.loc[i, '2.3.5'], df_p.loc[i, '2.3.6'], df_p.loc[i, '2.3.7'], df_p.loc[i, '2.3.8'])

    p1 = and_gate(df_p.loc[i, '3.8'], df_p.loc[i, '5.2'])
    p2 = and_gate(df_p.loc[i, '4.1'], df_p.loc[i, '4.2'], df_p.loc[i, '4.4'])
    p3 = and_gate(df_p.loc[i, '3.6'], df_p.loc[i, '5.3'], df_p.loc[i, '5.4'])
    p4 = or_gate(p6, df_p.loc[i, '3.3'], df_p.loc[i, '3.4'], df_p.loc[i, '3.5'])
    p5 = and_gate(df_p.loc[i, '3.7'], df_p.loc[i, '3.9'], df_p.loc[i, '4.3'], df_p.loc[i, '4.5'])

    g1 = or_gate(p1, df_p.loc[i, '5.5'])
    g2 = or_gate(p2, p3, p4, p5)

    p = and_gate(g1, g2)

    df_p.loc[i, 'p_ransomware_FTA'] = round(p, 3)


# risk 2
for i in df_p.index:
    p7 = max(df_p.loc[i, '2.2.1'], df_p.loc[i, '2.2.2'], df_p.loc[i, '2.2.3'], df_p.loc[i, '2.2.4'],
                 df_p.loc[i, '2.2.5'], df_p.loc[i, '2.2.6'], df_p.loc[i, '2.2.7'], df_p.loc[i, '2.2.8'],)

    p8 = max(df_p.loc[i, '2.3.1'], df_p.loc[i, '2.3.2'], df_p.loc[i, '2.3.3'], df_p.loc[i, '2.3.4'],
                 df_p.loc[i, '2.3.5'], df_p.loc[i, '2.3.6'], df_p.loc[i, '2.3.7'], df_p.loc[i, '2.3.8'],)

    p1 = and_gate(df_p.loc[i, '3.8'], df_p.loc[i, '5.2'])
    p2 = and_gate(p7, df_p.loc[i, '2.4'])
    p3 = and_gate(df_p.loc[i, '1.7'], df_p.loc[i, '5.1'])
    p4 = and_gate(df_p.loc[i, '1.3'], df_p.loc[i, '3.6'], df_p.loc[i, '5.3'], df_p.loc[i, '5.4'])
    p5 = or_gate(p8, df_p.loc[i, '3.3'], df_p.loc[i, '3.4'], df_p.loc[i, '3.5'])
    p6 = and_gate(df_p.loc[i, '3.7'], df_p.loc[i, '3.9'], df_p.loc[i, '4.3'], df_p.loc[i, '4.5'])

    g1 = or_gate(p1, df_p.loc[i, '5.5'], p2, p3)
    g2 = or_gate(p4, p5, p6)

    p = and_gate(g1, g2)

    df_p.loc[i, 'p_phishing_FTA'] = round(p, 3)


# risk 3
for i in df_p.index:
    p8 = max(df_p.loc[i, '2.2.1'], df_p.loc[i, '2.2.2'], df_p.loc[i, '2.2.3'], df_p.loc[i, '2.2.4'],
                 df_p.loc[i, '2.2.5'], df_p.loc[i, '2.2.6'], df_p.loc[i, '2.2.7'], df_p.loc[i, '2.2.8'],)

    p9 = max(df_p.loc[i, '2.3.1'], df_p.loc[i, '2.3.2'], df_p.loc[i, '2.3.3'], df_p.loc[i, '2.3.4'],
                 df_p.loc[i, '2.3.5'], df_p.loc[i, '2.3.6'], df_p.loc[i, '2.3.7'], df_p.loc[i, '2.3.8'],)

    p1 = and_gate(df_p.loc[i, '3.8'], df_p.loc[i, '5.2'])
    p2 = and_gate(p8, df_p.loc[i, '2.4'], df_p.loc[i, '1.5'], df_p.loc[i, '5.7'], df_p.loc[i, '5.6'])
    p3 = and_gate(df_p.loc[i, '1.7'], df_p.loc[i, '5.1'], df_p.loc[i, '5.5'])
    
    p4 = and_gate(df_p.loc[i, '4.1'], df_p.loc[i, '4.2'], df_p.loc[i, '4.4'])
    p5 = and_gate(df_p.loc[i, '1.3'], df_p.loc[i, '3.6'], df_p.loc[i, '5.3'], df_p.loc[i, '5.4'])
    p6 = or_gate(p9, df_p.loc[i, '3.3'], df_p.loc[i, '3.4'], df_p.loc[i, '3.5'])
    p8 = and_gate(df_p.loc[i, '3.7'], df_p.loc[i, '3.9'], df_p.loc[i, '4.3'], df_p.loc[i, '4.5'])

    g1 = or_gate(p1, p2, p3)
    g2 = or_gate(p4, p5, p6, p7)

    p = and_gate(g1, g2)

    df_p.loc[i, 'p_insider_FTA'] = round(p, 3)


# risk 4
for i in df_p.index:

    p7 = max(df_p.loc[i, '2.3.1'], df_p.loc[i, '2.3.2'], df_p.loc[i, '2.3.3'], df_p.loc[i, '2.3.4'],
                 df_p.loc[i, '2.3.5'], df_p.loc[i, '2.3.6'], df_p.loc[i, '2.3.7'], df_p.loc[i, '2.3.8'],)

    p1 = and_gate(df_p.loc[i, '3.8'], df_p.loc[i, '5.2'])
    p2 = and_gate(df_p.loc[i, '1.7'], df_p.loc[i, '5.1'])

    p3 = and_gate(df_p.loc[i, '4.1'], df_p.loc[i, '4.4'])
    p4 = and_gate(df_p.loc[i, '1.3'], df_p.loc[i, '3.6'], df_p.loc[i, '5.3'], df_p.loc[i, '5.4'])
    p5 = or_gate(p7, df_p.loc[i, '3.3'], df_p.loc[i, '3.4'], df_p.loc[i, '3.5'])
    p6 = and_gate(df_p.loc[i, '3.7'], df_p.loc[i, '3.9'], df_p.loc[i, '4.3'], df_p.loc[i, '4.5'])

    g1 = or_gate(p1, df_p.loc[i, '5.5'], p2, df_p.loc[i, '2.4'])
    g2 = or_gate(p3, p4, p5, p6)

    p = and_gate(g1, g2)

    df_p.loc[i, 'p_data_FTA'] = round(p, 3)


# risk 5
for i in df_p.index:

    p6 = max(df_p.loc[i, '2.3.1'], df_p.loc[i, '2.3.2'], df_p.loc[i, '2.3.3'], df_p.loc[i, '2.3.4'],
                 df_p.loc[i, '2.3.5'], df_p.loc[i, '2.3.6'], df_p.loc[i, '2.3.7'], df_p.loc[i, '2.3.8'],)

    p1 = and_gate(df_p.loc[i, '3.8'], df_p.loc[i, '5.2'])
    p2 = and_gate(df_p.loc[i, '5.5'], df_p.loc[i, '5.1'])

    p3 = and_gate(df_p.loc[i, '1.3'], df_p.loc[i, '3.6'], df_p.loc[i, '5.3'], df_p.loc[i, '5.4'])
    p4 = or_gate(p6, df_p.loc[i, '3.3'], df_p.loc[i, '3.4'], df_p.loc[i, '3.5'])
    p5 = and_gate(df_p.loc[i, '3.7'], df_p.loc[i, '3.9'], df_p.loc[i, '4.3'], df_p.loc[i, '4.5'])

    g1 = or_gate(p1, p2)
    g2 = or_gate(df_p.loc[i, '4.2'], p3, p4, p5)

    p = and_gate(g1, g2)

    df_p.loc[i, 'p_supply_FTA'] = round(p, 3)




