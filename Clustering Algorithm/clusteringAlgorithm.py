#This function takes two points as input and returns the distance between them
def distanceCalculator(point1,point2):
    return ((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)**0.5

#This function takes a cluster of points as an input and calculates and returns their mean
def mean(cluster):
    x = sum([i[0] for i in cluster])/len(cluster)
    y = sum([i[1] for i in cluster])/len(cluster)
    return (x,y)

dataSet = [(0,0),(1,0),(1,1),(0,1),(-1,0)]
centroid1 = (1,0)
centroid2 = (1,1)

#This loop will run for 2 times to check if we are getting the same clusters and centroids in second
#iteration as we got in first iteration.
for i in range(0,2):
    print("\nIteration number {}\n".format(i+1))
    cluster1 = []
    cluster2 = []
    #This loop will run for every points in the dataset and compare the distance between each point and 
    #centroid of each clusters, and will save the point in the cluster which in nearest to this point.
    for j in range(0,len(dataSet)):
        if distanceCalculator(dataSet[j],centroid1)<=distanceCalculator(dataSet[j],centroid2):
            cluster1.append(dataSet[j])
        else:
            cluster2.append(dataSet[j])
    centroid1 = mean(cluster1)
    centroid2 = mean(cluster2)
    print("Cluster 1 : ",cluster1)
    print("Cluster 2 : ",cluster2)
    print("Centroid 1 : ",centroid1)
    print("Centroid 2 : ",centroid2)