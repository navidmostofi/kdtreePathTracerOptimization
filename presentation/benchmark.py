import matplotlib.pyplot as plt
import numpy as np


p1 = [[53.452290, 49.272064, 51.599041, 41.238239],
[53.342525, 49.222210, 51.333378, 40.039585],
[53.728256, 49.484932, 51.795837, 41.268188],
[53.464287, 49.302368, 52.001152, 40.854973],
[53.717186, 49.206203, 51.961155, 40.770596],
[53.479683, 49.136894, 51.565025, 40.837376],
[53.563648, 49.361565, 51.504547, 40.490593],
[53.363300, 49.186783, 51.538589, 41.069954],
[53.492348, 49.367519, 52.097538, 40.588032],
[53.527489, 49.231102, 51.967682, 41.132641]]


p2 = [[78.853249, 72.754364, 56.752930, 43.924160],
[78.936737, 72.921753, 56.241920, 43.218620],
[79.048477, 73.034882, 56.759136, 43.839615],
[79.196037, 72.940826, 56.665955, 44.169857],
[78.925568, 72.817818, 56.830082, 44.133667],
[79.035522, 72.919998, 56.125153, 44.419807],
[79.050240, 72.760834, 56.374622, 44.438622],
[79.042618, 73.086136, 56.896160, 43.818302],
[78.956474, 72.923492, 56.390976, 43.797508],
[79.035103, 73.065025, 57.168766, 44.327679]]


p3 = [[155.846344, 143.690872, 68.146011, 49.671108],
[155.825073, 143.762238, 67.882370, 48.514397],
[156.267471, 143.715240, 69.242523, 49.765507],
[156.124802, 144.248718, 69.118752, 49.468197],
[156.016357, 143.864029, 70.088188, 50.534496],
[155.924194, 143.771561, 69.018112, 50.287521],
[155.953827, 143.872665, 68.828575, 49.283905],
[156.139496, 143.876892, 68.742561, 49.527359],
[156.066147, 143.859833, 69.988609, 49.601055],
[156.003845, 144.101517, 69.601181, 50.125374]]


p4 = [[315.254059, 295.667053, 93.522079, 58.779938],
[315.306122, 291.646729, 91.767975, 57.549667],
[315.429718, 295.767517, 93.592896, 59.016479],
[315.527161, 295.698090, 95.368385, 59.534847],
[315.162170, 295.399170, 95.915260, 60.660225],
[315.521698, 291.961884, 95.745148, 59.230145],
[315.409149, 291.520813, 94.456963, 58.782433],
[315.567413, 295.591370, 94.761543, 58.822624],
[315.161407, 295.286530, 94.372513, 58.532829],
[315.314362, 295.972473, 92.888199, 59.001152]]


p5 = [[641.841797, 592.676941, 134.830750, 79.795837],
[641.546936, 593.308105, 130.970718, 77.705307],
[642.534424, 592.676880, 137.645401, 78.838364],
[642.145691, 593.097473, 137.855225, 78.963196],
[642.129150, 592.659180, 137.480988, 81.677467],
[642.068481, 593.411133, 135.646088, 78.810333],
[642.421631, 593.182678, 137.738617, 79.987297],
[641.961609, 592.932861, 137.178757, 78.317093],
[642.166626, 592.748718, 136.812408, 79.505447],
[642.689575, 592.885986, 137.911423, 79.929176]]


p6 = [[2281.165283, 2180.721680, 212.943924, 116.712990],
[2280.900879, 2180.258545, 208.482117, 113.440872],
[2281.699951, 2182.276123, 215.839905, 118.723839],
[2280.524414, 2183.135010, 218.825912, 119.403831],
[2281.018555, 2181.421875, 220.689209, 121.430122],
[2280.698730, 2181.740723, 218.186066, 122.408318],
[2280.429688, 2181.965332, 214.664719, 119.276039],
[2280.663086, 2181.996338, 216.239044, 114.977180],
[2280.578369, 2180.654297, 216.630615, 118.388641],
[2281.381104, 2181.621582, 216.799942, 118.700966]]


p7 = [[3556.819092, 3361.569336, 378.477875, 194.881500],
[3557.768799, 3360.592285, 366.524597, 191.307190],
[3558.853760, 3361.468262, 389.975555, 196.996017],
[3557.284424, 3360.384521, 389.518127, 196.972275],
[3558.567139, 3359.667480, 389.575409, 198.127502],
[3557.649414, 3358.281006, 377.177643, 205.304962],
[3558.996582, 3357.858643, 382.524841, 196.306854],
[3557.598633, 3362.512451, 389.808594, 190.609055],
[3557.660400, 3359.337158, 381.883789, 194.983322],
[3557.803955, 3361.268311, 378.545288, 194.990631]]


p8 = [[99999.000000, 99999.000000, 696.824219, 337.702118],
[99999.000000, 99999.000000, 675.081726, 320.391083],
[99999.000000, 99999.000000, 694.614441, 344.573364],
[99999.000000, 99999.000000, 707.251953, 343.722870],
[99999.000000, 99999.000000, 713.409607, 351.965515],
[99999.000000, 99999.000000, 704.823975, 353.936035],
[99999.000000, 99999.000000, 701.153381, 344.329956],
[99999.000000, 99999.000000, 702.913025, 349.185974],
[99999.000000, 99999.000000, 704.176758, 332.633698],
[99999.000000, 99999.000000, 694.627502, 345.728424]]


# averages:
pp1 = np.sum(np.array(p1), axis = 0) / len(p1)
pp2 = np.sum(np.array(p2), axis = 0) / len(p2)
pp3 = np.sum(np.array(p3), axis = 0) / len(p3) 
pp4 = np.sum(np.array(p4), axis = 0) / len(p4)
pp5 = np.sum(np.array(p5), axis = 0) / len(p5)
pp6 = np.sum(np.array(p6), axis = 0) / len(p6)
pp7 = np.sum(np.array(p7), axis = 0) / len(p7)
pp8 = np.sum(np.array(p8), axis = 0) / len(p8)

print pp1
print pp2
print pp3
print pp4
print pp5
print pp6
print pp7
print pp8





# Data to plot
labels = ['vertexTandA', 'scanline', 'aa', 'render']
colors = ['#005511', '#002244', '#004477', '#118899']
explode = (0.1, 0.5, 0.2, 0.1)


P = [pp1, pp2, pp3, pp4, pp5, pp6, pp7, pp8]
titles = ['optimized\nfunctions time percentage', 
          'aabb only\nfunctions time percentage', 
          'backface cull\nfunctions time percentage', 
          'no opt\nfunctions time percentage',
          'MSAA 4x opt\nfunctions time percentage',
          'MSAA4x no opt\nfunctions time percentage',
          'SSAA opt\nfunctions time percentage',
          'SSAA no opt\nfunctions time percentage']


for i in range(8):
    sizes = P[i]
    
    percent = 100.*P[i]/P[i].sum()

    print percent

    # Plot
    fig = plt.figure(facecolor='black')
    #fig.patch.set_alpha(1.0)
    fig.patch.set_facecolor('black')
    plt.rcParams['text.color'] = 'gray'
    plt.rcParams['axes.facecolor'] = 'black'
    plt.rcParams['lines.linewidth'] = 4

    ax = plt.subplot(111, axisbg='black')
    
    pie = ax.pie(sizes, explode=explode, colors=colors, textprops = {'color':'#aaaaaa', 'fontweight':'bold'},
            autopct='%1.1f%%', shadow=True, startangle=140)



    ax.set_ylabel('Test Benchmark Averages', color = '#338888', fontweight='bold')
    ax.set_title(titles[i])
    ax.patch.set_facecolor('black') 
    ax.axis('equal')

    percentlabels = list(labels)
    for j in range(len(percentlabels)):
        percentlabels[j] += (' %.1f' % percent[j])+'''%'''

    plt.legend(pie[0], percentlabels, loc='upper left')

    plt.savefig('piechart_%d.png' % i, bbox_inches='tight', facecolor='black')
    #plt.show()
    




fig = plt.figure(facecolor='black')
#fig.patch.set_alpha(1.0)
fig.patch.set_facecolor('black')
plt.rcParams['text.color'] = 'gray'
plt.rcParams['axes.facecolor'] = 'black'
plt.rcParams['lines.linewidth'] = 4

N = 8
t1 = [pp1[0], pp2[0], pp3[0], pp4[0], pp5[0], pp6[0], pp7[0], pp8[0]]
t2 = [pp1[1], pp2[1], pp3[1], pp4[1], pp5[1], pp6[1], pp7[1], pp8[1]]
t3 = [pp1[2], pp2[2], pp3[2], pp4[2], pp5[2], pp6[2], pp7[2], pp8[2]]
t4 = [pp1[3], pp2[3], pp3[3], pp4[3], pp5[3], pp6[3], pp7[3], pp8[3]]

ind = np.arange(N)    # the x locations for the groups
width = 0.8       # the width of the bars: can also be len(x) sequence

pl1 = plt.bar(ind, t1, width, color='#004466')
pl2 = plt.bar(ind, t2, width, color='#006699', bottom=t1 )
pl3 = plt.bar(ind, t3, width, color='#11aa88', bottom=t2 )
pl4 = plt.bar(ind, t4, width, color='#ff5555', bottom=t3 )

plt.ylabel('Time in ms', color = '#338888', fontweight='bold')
plt.title('Optimization and post processing benchmark')
plt.xticks(ind + width/2., ('optimized', 
                            'aabb\nonly', 
                            'backface\ncull', 
                            'no opt',
                            'MSAA 4x\nopt',
                            'MSAA4x\nno opt',
                            'SSAA\nopt',
                            'SSAA\nno opt'),
            color = '#333333',
            fontweight='bold')

plt.yticks(np.arange(0, 1000, 100), color = '#333333', fontweight='bold')
plt.legend([pl1[0], pl2[0], pl3[0], pl4[0]], labels, loc=0)

plt.savefig('boxchart.png', bbox_inches='tight', facecolor='black')
#plt.show()





# no scanline





