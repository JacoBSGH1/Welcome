import os
import pandas as pd
proteins_path = os.path.join("..","data","AlphaLasso_20261030_203453.tsv")
# a)
pLDDT_loop_proteins = pd.read_csv(proteins_path, sep='\t',usecols=[5,7,8])
loop_proteins_dict = pLDDT_loop_proteins.to_dict(orient='list')

def loops_average(file):
    loops_sum = 0
    for value in loop_proteins_dict.values():
        loops_sum += sum(value)
    return loops_sum/(3*len(pLDDT_loop_proteins))

print(f'Overall average of the 2 added columns (Loop_area, Loop_length) and the pLDDT_chain: {loops_average(loop_proteins_dict)}')

# b)
pLDDT_loop_proteins_B = pd.read_csv(proteins_path, sep='\t',usecols=[0,5,7,8])

groups = pLDDT_loop_proteins_B.columns[0]

for i in range(len(pLDDT_loop_proteins_B)):
    name = pLDDT_loop_proteins_B.loc[i, groups]
    for number in ['4','5','6','7','8']:
        if number in name:
            pLDDT_loop_proteins_B.loc[i, groups] = "L" + number
            break

pLDDT_loop_proteins_B_dict = pLDDT_loop_proteins_B.to_dict(orient='records')

L4_sum, L5_sum, L6_sum, L7_sum, L8_sum = 0,0,0,0,0
L4_count, L5_count, L6_count, L7_count, L8_count = 0,0,0,0,0
for record in pLDDT_loop_proteins_B_dict:
    lasso_type = record['#Lasso_type']
    if lasso_type == "L4":
        L4_sum = L4_sum + record['pLDDT_chain'] + record['Loop_length'] + record['Loop_area']
        L4_count += 1
    if lasso_type == "L5":
        L5_sum = L5_sum + record['pLDDT_chain'] + record['Loop_length'] + record['Loop_area']
        L5_count += 1
    if lasso_type == "L6":
        L6_sum = L6_sum + record['pLDDT_chain'] + record['Loop_length'] + record['Loop_area']
        L6_count += 1
    if lasso_type == "L7":
        L7_sum = L7_sum + record['pLDDT_chain'] + record['Loop_length'] + record['Loop_area']
        L7_count += 1
    if lasso_type == "L8":
        L8_sum = L8_sum + record['pLDDT_chain'] + record['Loop_length'] + record['Loop_area']
        L8_count += 1
    else:
        continue

L4_average = L4_sum/ (3 * L4_count)
L5_average = L5_sum/ (3 * L5_count)
L6_average = L6_sum/ (3 * L6_count)
L7_average = L7_sum / (3 * L7_count)
L8_average = L8_sum / (3 * L8_count)

print(f'L4_average: {L4_average}, L5_average: {L5_average}, L6_average: {L6_average}, L7_average: {L7_average}, L8_average: {L8_average}')
lasso_proteins_stats = os.path.join('..', 'data', 'lasso_proteins_stats.csv')
f = open(lasso_proteins_stats, 'w')
f.write('Type,Overall Average\n')
f.write(f'L4,{L4_average}\nL5,{L5_average}\nL6,{L6_average}\nL7,{L7_average}\nL8,{L8_average}\nAll,{loops_average(loop_proteins_dict)}\n')
f.close()


'''
# b) - crazy Claude commands - checked it out of interest on how to do it actually efficiently
plDDT_loop_proteins_grouped = pd.read_csv(proteins_path, sep='\t',usecols=[0,5,7,8])
def average_loop_proteins_grouped(file):
    rows = plDDT_loop_proteins_grouped.to_dict(orient='records')
    type_col = plDDT_loop_proteins_grouped.columns[0]
    value_cols = list(plDDT_loop_proteins_grouped.columns[1:])
    collected = {}
    for row in rows:
        main_type = "L" + row[type_col][2]      # "L+4N" -> "L4"
        if main_type not in collected:
            collected[main_type] = {col: [] for col in value_cols}
        for col in value_cols:
            collected[main_type][col].append(row[col])

    sums_grouped = {}
    for main_type, columns in collected.items():
        sums_grouped[main_type] = {}
        for col, values in columns.items():
            sums_grouped[main_type][col] = sum(values)

    overall_averages = {}
    for main_type, columns in collected.items():
        total = 0
        count = 0
        for col, values in columns.items():
            total += sum(values)
            count += len(values)
        overall_averages[main_type] = total / count

    return overall_averages

print(f'Overall average of the 2 added columns (Loop_area, Loop_length) and the pLDDT_chain, by groups: \n {average_loop_proteins_grouped(plDDT_loop_proteins_grouped)}')
'''