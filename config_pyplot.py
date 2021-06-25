from matplotlib import rcParams
from matplotlib.ticker import MaxNLocator
from matplotlib import pyplot as plt


def config_matplotlib():
    font_size = 10
    plt.rc('font', serif='Times')
    rcParams['axes.labelsize'] = font_size*1.5
    rcParams['xtick.labelsize'] = font_size
    rcParams['ytick.labelsize'] = font_size
    rcParams['legend.fontsize'] = font_size
    plt.rcParams['axes.spines.top'] = True
    plt.rcParams['axes.spines.bottom'] = True
    plt.rcParams['axes.spines.left'] = True
    plt.rcParams['axes.spines.right'] = True
    rcParams['lines.linewidth'] = 2
    rcParams['font.family'] = 'times'
    rcParams['font.serif'] = ['Computer Modern Roman']
    rcParams['text.usetex'] = False # if latex is available change to True  
    
    rcParams['axes.linewidth'] = 1.0
    
    rcParams['xtick.top'] = True   # draw ticks on the top side
    rcParams['xtick.major.size'] = 6.0
    rcParams['xtick.minor.size'] = 4.0
    rcParams['xtick.major.width'] = 1.0
    rcParams['xtick.minor.width'] = 0.8
    rcParams['xtick.direction'] = 'in'
    
    
    rcParams['ytick.left'] = True    # draw ticks on the left side
    rcParams['ytick.right'] = True   # draw ticks on the right side
    rcParams['ytick.labelleft'] = True    # draw tick labels on the left side
    rcParams['ytick.labelright'] = False   # draw tick labels on the right side
    rcParams['ytick.major.size'] = 6.0     # major tick size in points
    rcParams['ytick.minor.size'] = 4.0      # minor tick size in points
    rcParams['ytick.major.width'] = 1.0     # major tick width in points
    rcParams['ytick.minor.width'] = 0.8
    rcParams['ytick.direction'] = 'in'
    
    #ax.set_xticks([2,4,6,8,10])
    #my_locator = MaxNLocator(6)
    # Set up axes and plot some awesome science
    #ax.yaxis.set_major_locator(my_locator)
