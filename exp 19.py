import numpy as np
import scipy.stats as stats

drug = [8,10,9,7,11]
placebo = [3,4,2,5,3]

ci_drug = stats.t.interval(0.95,len(drug)-1,
           loc=np.mean(drug),scale=stats.sem(drug))

ci_placebo = stats.t.interval(0.95,len(placebo)-1,
              loc=np.mean(placebo),scale=stats.sem(placebo))

print("Drug CI:",ci_drug)
print("Placebo CI:",ci_placebo)
