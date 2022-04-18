#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Kiran Kumar Thingbaijam"
__email__ = "thingbaijam@gmail.com"

import matplotlib.pyplot as plt
import numpy as np

"""
pltornado(cases, ...)

plots a tornado diagram for the input - cases which is dictionary of the format:

```
cases = {
 '<parameter1>': {'inputs': [<..,>],
              'results':[<..,>],
              'base': <var>,
             },
  ....
}
```

An wrapper can be easiy implemented when the data is in either json or toml format.

Other key arguments are as follows.

- plot_orient: The orientation of the plot which can equal to 'horizontal' (default) or 'vertical'

- barwidth: The width of the bars. The defualt value is 0.8.

- xlim: The range defining the bounds of the x-axis. The default is [-50, 50].

- xypad: The padding for bar annotations. The defualt is (1.0, 0.1),

- sort_spread: The sorting of the bar plots based on the spread of the results 
               across the base result. This can set either as None, 'ascend' or 'descend'. 
               The default is None.
- title: The title of the plot.

- ylabel: The label on the y-axis

- xlabel: The label on the x-axis

- ax: A singe axes for plotting. If it is equal to None (default), a single axes is created. 


"""


def plot(cases, plot_orient='horizontal', barwidth = 0.8, \
                xlim = [-50, 50], xypad = (1.0, 0.1), \
                sort_spread = None, \
                title='', ylabel='', xlabel='', ax=None):
    
    xpad, ypad = xypad
    if ax is None:
        fig, ax = plt.subplots(figsize=(6,6))
        plt.rcParams.update({'font.size': 12})

    for case in cases:
        results = cases[case]['results']
        base = cases[case]['base']
        spread = [var-base for var in results]
        cases[case]['spreads']= spread
        cases[case]['spread_range']= max(spread)-min(spread)
        cases[case]['results'] = results

    # sort the cases by the spread ranges, if required
    mycases = [key for key in cases.keys()]
    
    if sort_spread is not None:
        spread_ranges = [cases[case]['spread_range'] for case in mycases]
        if sort_spread=='ascend':
            idexs = np.argsort(np.array(spread_ranges))
        else:
            idexs = np.argsort(-np.array(spread_ranges))
        tcases = []
        for indx in idexs:
            tcases.append(mycases[indx])
        mycases = tcases
    #
    ypos = [k-ypad for k in range(len(mycases))]

    for case, yp in zip(mycases, ypos):
        xx = cases[case]['spreads']
        yy = [case]*len(xx)
    
        inputs = cases[case]['inputs']
        if inputs is None:
            inputs = ['']*len(xx)
        
        for x, y, inps in zip(xx,yy, inputs):
        
            if plot_orient=='vertical':
                if x<=0:
                    ax.bar(y,x, barwidth, alpha=0.5, color = 'c', edgecolor='k')
                    if x!=0:
                        ax.text(yp, x-xpad, str(inps))
                else:
                    ax.bar(y,x, barwidth, alpha=0.5, color = 'r', edgecolor='k')
                    if x!=0:
                        ax.text(yp, x+xpad, str(inps))
            else:
                if x<=0:
                    ax.barh(y,x, barwidth, alpha=0.5, color = 'c', edgecolor='k')
                    if x!=0:
                        ax.text(x-xpad-2*len(str(inps)), yp, str(inps))
                else:
                    ax.barh(y,x, barwidth, alpha=0.5, color = 'r', edgecolor='k')
                    if x!=0:
                        ax.text(x+xpad, yp, str(inps))
            ax.set_xlim(xlim)
    ax.set_title(title)
    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)

