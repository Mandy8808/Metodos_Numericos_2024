######
# CONFIGURACION QUE USO PARA GRAFICAR
####

# MODULOS
import matplotlib as mpl
import matplotlib.font_manager as font_manager

from cycler import cycler


def general():
    """
    CONFIGURACIÓN GENERAL
    """
    # CONFIGURACIÓN GENERAL

    # Figura
    # mpl.rcParams['figure.dpi'] = 100 # figure dots per inch
    mpl.rcParams['figure.figsize'] = [12, 9]  # [4,3]
    mpl.rcParams['figure.facecolor'] = 'white'     # figure facecolor
    mpl.rcParams['figure.edgecolor'] = 'white'     # figure edgecolor
    mpl.rcParams['savefig.dpi'] = 100

    # estilo de linea y grosor
    mpl.rcParams['lines.linestyle'] = '-'
    mpl.rcParams['lines.linewidth'] = 2.

    # orden de los colores que usará
    mpl.rcParams['axes.prop_cycle'] = cycler('color',
                                             ['#1f77b4', '#ff7f0e', '#2ca02c',
                                              '#d62728', '#9467bd', '#8c564b',
                                              '#e377c2', '#7f7f7f', '#bcbd22',
                                              '#17becf'])
    # latex modo math
    # Should be: 'dejavusans' (default), 'dejavuserif', 'cm' (Computer Modern),
    #             'stix', 'stixsans' or 'custom'
    mpl.rcParams['mathtext.fontset'] = 'cm'
    mpl.rcParams['mathtext.fallback'] = 'cm'

    # latex modo text
    # Should be: serif, sans-serif, cursive, fantasy, monospace
    mpl.rcParams['font.family'] = 'serif'
    cmfont = font_manager.FontProperties(fname=mpl.get_data_path()
                                         + '/fonts/ttf/cmr10.ttf')
    mpl.rcParams['font.serif'] = cmfont.get_name()
    mpl.rcParams['font.size'] = 16  # size of the text

    # Display axis spines, (muestra la linea de los marcos)
    mpl.rcParams['axes.spines.left'] = True
    mpl.rcParams['axes.spines.bottom'] = True
    mpl.rcParams['axes.spines.top'] = True
    mpl.rcParams['axes.spines.right'] = True

    # axes numbers, etc.
    # 'large' tamaño de los números de las x, y
    mpl.rcParams['xtick.labelsize'] = 13
    mpl.rcParams['ytick.labelsize'] = 13
    # direction: {in, out, inout} señalamiento de los ejes
    mpl.rcParams['xtick.direction'] = 'out'
    mpl.rcParams['ytick.direction'] = 'out'
    # draw ticks on the top side (dibujar las divisiones arriba)
    mpl.rcParams['xtick.top'] = False
    mpl.rcParams['ytick.right'] = False
    # draw label on the top/bottom
    mpl.rcParams['xtick.labeltop'] = False
    mpl.rcParams['xtick.labelbottom'] = True
    # draw x axis bottom/top major ticks
    mpl.rcParams['xtick.major.top'] = False
    mpl.rcParams['xtick.major.bottom'] = True
    # draw x axis bottom/top minor ticks
    mpl.rcParams['xtick.minor.top'] = False
    mpl.rcParams['xtick.minor.bottom'] = False

    # mpl.rcParams['xtick.minor.visible'] = True # visibility of minor ticks on x-axis

    # labels and title
    mpl.rcParams['axes.titlepad'] = 6.0  # pad between axes and title in points
    mpl.rcParams['axes.labelpad'] = 3.0  # 10.0     # space between label and axis
    mpl.rcParams['axes.labelweight'] = 'normal'  # weight (grosor) of the x and y labels
    mpl.rcParams['axes.labelcolor'] = 'black'
    mpl.rcParams['axes.unicode_minus'] = False  # use Unicode for the minus symbol
    mpl.rcParams['axes.linewidth'] = 1  # edge linewidth, grosor del marco

    mpl.rcParams['axes.titlesize'] = 24  # title size
    mpl.rcParams['axes.labelsize'] = 15  # label size
    # mpl.rcParams['lines.markersize'] = 10  # weight of the marker

    # Legend
    mpl.rcParams['legend.loc'] = 'best'
    mpl.rcParams['legend.frameon'] = True  # if True, draw the legend on a background patch
    mpl.rcParams['legend.framealpha'] = 0.19  # 0.8 legend patch transparency
    mpl.rcParams['legend.facecolor'] = 'inherit'  # inherit from axes.facecolor; or color spec
    mpl.rcParams['legend.edgecolor'] = 'inherit' # background patch boundary color
    mpl.rcParams['legend.fancybox'] = True  # if True, use a rounded box for the

    # mpl.rcParams['legend.numpoints'] = 1 # the number of marker points in the legend line
    # mpl.rcParams['legend.scatterpoints'] = 1 # number of scatter points
    # mpl.rcParams['legend.markerscale'] = 1.0 # the relative size of legend markers vs. original
    mpl.rcParams['legend.fontsize'] = 15  # 'medium' 'large'
    mpl.rcParams['legend.title_fontsize'] = 13  # 'xx-small'

    # Dimensions as fraction of fontsize:
    mpl.rcParams['legend.borderpad'] = 0.4  # border whitespace espacio de los bordes con respecto al texto
    mpl.rcParams['legend.labelspacing'] = 0.5  # the vertical space between the legend entries
    mpl.rcParams['legend.handlelength'] = 1.5  # the length of the legend lines defauld 2
    # mpl.rcParams['legend.handleheight'] = 0.7  # the height of the legend handle
    mpl.rcParams['legend.handletextpad'] = 0.8  # the space between the legend line and legend text
    # mpl.rcParams['legend.borderaxespad'] = 0.5  # the border between the axes and legend edge
    # mpl.rcParams['legend.columnspacing'] = 8.0  # column separation

# latex
    mpl.rcParams['text.usetex'] = True
    mpl.rcParams['pgf.rcfonts'] = False
    mpl.rcParams['text.latex.preamble'] = r'\usepackage{amssymb}'  # , \usepackage{txfonts}
    mpl.rcParams['pgf.preamble'] = r'\usepackage{amssymb}'

    return


def latex():
    """
    para devolver estilo pgf
    """
    # estructura para latex
    mpl.use("pgf")
    mpl.rcParams['pgf.texsystem'] = 'pdflatex'

    return
###
