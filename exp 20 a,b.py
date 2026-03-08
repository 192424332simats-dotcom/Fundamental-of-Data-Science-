from scipy.stats import ttest_ind

A = [12,14,15,13,16]
B = [10,11,12,9,13]

t,p = ttest_ind(A,B)

print("p value:",p)

if p < 0.05:
    print("Significant difference")
else:
    print("No significant difference")
