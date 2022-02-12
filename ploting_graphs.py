##https://stats.stackexchange.com/questions/11984/how-can-i-remove-the-z-order-bias-of-a-coloured-scatter-plot

import matplotlib.pyplot as plt
import numpy as np

class ZBiasFreePlotter(object):
    def __init__(self):
        self.plot_calls = []

    def add_plot(self, f, xs, ys, *args, **kwargs):
        self.plot_calls.append((f, xs, ys, args, kwargs))

    def draw_plots(self, chunk_size=512):
        scheduled_calls = []
        for f, xs, ys, args, kwargs in self.plot_calls:
            assert(len(xs) == len(ys))
            index = np.arange(len(xs))
            np.random.shuffle(index)
            index_blocks = [index[i:i+chunk_size] for i in np.arange(len(index))[::chunk_size]]
            for i, index_block in enumerate(index_blocks):
                # Only attach a label for one of the chunks
                if i != 0 and kwargs.get("label") is not None:
                    kwargs = kwargs.copy()
                    kwargs["label"] = None
                scheduled_calls.append((f, xs[index_block], ys[index_block], args, kwargs))

        np.random.shuffle(scheduled_calls)

        for f, xs, ys, args, kwargs in scheduled_calls:
            f(xs, ys, *args, **kwargs)


fig, ax = plt.subplots(1, 1)
bias_free_plotter = ZBiasFreePlotter()

things_to_plot = [np.sin(x) for x in np.arange(0,2*(np.pi),0.1)]

for xs, ys, color in things_to_plot:
    bias_free_plotter.add_plot(ax.plot, xs, ys, c=color)

bias_free_plotter.draw_plots()
