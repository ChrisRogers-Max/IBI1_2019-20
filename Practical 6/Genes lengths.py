# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 16:48:47 2020

@author: 92801
"""

gene_lengths=[9410,3944141,4442,105338,19149,76779,126550,36296,842,15981]
gene_lengths.sort()

del(gene_lengths[0])
gene_lengths.pop()
print(gene_lengths)

import matplotlib.pyplot as plt
plt.boxplot(gene_lengths,notch=False,vert=True,whis=1.5,patch_artist=True,meanline=False,showmeans=True,showcaps=True,showbox=True,showfliers=True)
plt.show()