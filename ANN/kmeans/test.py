from pylab import plot,show
from numpy import vstack,array
from numpy.random import rand
from scipy.cluster.vq import kmeans,vq
import matplotlib.pyplot as plt

# data generation
data = vstack((rand(150,2) + array([.5,.5]),rand(150,2)))
#print (data)

# plt.figure(1)

# plt.subplot(211)
# plot(data,'ob')

# # # computing K-Means with K = 2 (2 clusters)
# # centroids,_ = kmeans(data,2)
# # # assign each sample to a cluster
# # idx,_ = vq(data,centroids)

# # plt.subplot(212)
# # #some plotting using numpy's logical indexing
# # plot(data[idx==0,0],data[idx==0,1],'ob',
# #      data[idx==1,0],data[idx==1,1],'or')
# # plot(centroids[:,0],centroids[:,1],'sg',markersize=8)


# # now with K = 3 (3 clusters)
# plt.subplot(212)
# centroids,_ = kmeans(data,3)
# idx,_ = vq(data,centroids)

# plot(data[idx==0,0],data[idx==0,1],'ob',
#      data[idx==1,0],data[idx==1,1],'or',
#      data[idx==2,0],data[idx==2,1],'og') # third cluster points
# plot(centroids[:,0],centroids[:,1],'sm',markersize=8)


# show()

a = [1,2,3,4,5]
b = [1,4,9,16,25]

plt.plot(a, b, 'ro')
plt.text(4, 16, "brother")
plt.show()