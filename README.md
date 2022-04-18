# butterfly

A python script to plot Butterfly (aka Tornado) diagrams, using matplotlib.pyplot

butterfly.plot(cases, ...)

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
- barwidth: The width of the bars. The default value is 0.8.
- xlim: The range defining the bounds of the x-axis. The default is [-50, 50].
- xypad: The padding for bar annotations. The default is (1.0, 0.1),
- sort_spread: The sorting of the bar plots based on the spread of the results 
               across the base result. This can set either as None, 'ascend' or 'descend'. 
               The default is None.
- title: The title of the plot.
- ylabel: The label on the y-axis
- xlabel: The label on the x-axis
- ax: A singe axes for plotting. If it is equal to None (default), a single axes is created. 

An example:

```
import butterfly

cases = {
    'parameter1': {'inputs': ['base','low','high'],
              'results':[25,40, 55],
              'base': 40,
             },
    'parameter2': {'inputs': ['left','mid','right'],
              'results':[2, 26, 30],
              'base': 26,
             },
    'parameter3': {'inputs': None,
              'results':[23, 40, 70],
              'base': 40,
             },
    'parameter4': {'inputs': None,
              'results':[12, 25, 26],
              'base': 25,
             },
    }

butterfly.plot(cases, plot_orient='horizontal', barwidth = 0.8, \
                xlim = [-50, 50], xypad = (1.0, 0.1), \
                sort_spread = 'ascend', \
                title='Test1', ylabel='cases', xlabel='range', ax=None)
```

![image](https://user-images.githubusercontent.com/42269445/163799551-e8b661c0-9633-4537-ac2c-9bf2bed07455.png)

