[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)


Using the variable totalwgt_lb, investigate whether first babies are lighter or heavier than others. Compute Cohen’s d to quantify the difference between the groups. How does it compare to the difference in pregnancy length?


``` python
import numpy as np
import nsfg

preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]

firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

print(np.mean(firsts['totalwgt_lb']),';', np.mean(others['totalwgt_lb']))
print(np.mean(firsts['totalwgt_lb']) - np.mean(others['totalwgt_lb']))

###calculate Cohen's d

def cohenD(group1, group2):
    
    m1, m2 = np.mean(group1), np.mean(group2)
    
    vars = [np.var(group1), np.var(group2)]
    weights = [len(group1), len(group2)]
    pooled_var = np.dot(vars, weights) / np.sum(weights)
    
    return (m1 - m2) / pooled_var**0.5
    
print(cohenD(firsts['totalwgt_lb'], others['totalwgt_lb']))
print(cohenD(firsts['prglngth'], others['prglngth']))
```

The Cohen's d for pregnancy length between first babies and not first babies was .029 standard deviations.

The Cohen's d for weight between first babies and not first babies was -.089.

This implies that the effect of being a first baby has a greater impact on birth weight than it does pregnancy length.
The sign of Cohen's d also leads to the conclusion that being a first baby reduces birthweight while it increases the pregnancy length.
