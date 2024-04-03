import matplotlib.pyplot as plt
import numpy as np
import cpuinfo
import os
import datetime

mem_bytes = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES')
mem_gib = int(mem_bytes/(1024.**3))

past_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")

#x = [1,2,0]
#y = [1,2,-2]
x,y = np.loadtxt('data.txt', delimiter=' ', unpack=True)

fig, ax = plt.subplots()
#ax.hist2d(x, y, bins=(np.arange(-3, 3, 0.1), np.arange(-3, 3, 0.1)))
ax.hist2d(x, y, bins=(np.arange(0, 300, 2), np.arange(0, 30, 0.5)))

#plt.scatter(x,y)  #generowanie punktow

#labels
plt.xlabel('TXS in block')
plt.ylabel('BLOCK TIME [ms]')
ax.set_title(cpuinfo.get_cpu_info()['brand_raw'] + ' + ' +  str(mem_gib) + 'GB RAM' )

plt.savefig(past_day+'.png')   # save the figure to file
plt.close(fig)

#print (dir + past_day )
