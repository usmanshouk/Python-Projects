#Usman Shoukat
#20153600
def fifo():
    """
    fifo function is searching for every page of request in cache, if it is missing in cache then it is 
    priting miss and adding it into cache provided that the cache is not full. If cache is full then then it removes the
    the page that has been in cache for longer period of time. And if the page requested is already in cache then
    it simply prints hit and don't do any changing to cache.
    """
    print()
    for i in request: #loop iterating through every page of request
        if i not in cache: #checking if page is in cache
            print("Miss :",i)
            if len(cache) <8: #if cache has space, simply add page to cache
                cache.append(i)
            else:               #otherwise remove the longer stayed and add new one
                cache.pop(0)
                cache.append(i)
        else:                   #if page is already in cache then just print that out
            print("Hit :",i)
        print(cache)
    print("\nCache List : ",cache)

def lfo():
    """
    lfu function is searching for every page of request in cache, if it is missing in cache then it is priting
    miss and adding it into cache provided that the cache is not full. If cache is full then then it removes the
    the page that has lowest number of hits and has been in cache for longer period of time. And if the page
    requested is already in cache then it simply prints hit and increase the number of hits of that 
    particular page in the cache.
    """
    print()
    for i in request: #loop iterating through every page of request
        if i not in [j[0] for j in cache]: #checking if page is in cache
            print("Miss :",i)
            if len(cache) <8: #if cache has space, simply add page to cache and set its hitting frequecy to 1
                cache.append([i,1])
            else: #otherwise remove the one with lowest number of hits and that stayed for longer period
                freq = [j[1] for j in cache] #list of number of hits
                index = freq.index(min(freq)) #getting the index of page with lowest number of hits
                cache.pop(index) #removing the one with lowest number of hits
                cache.append([i,1]) #adding the new page to the cache
        else: #if page is already in cache then it is increasing the number of hits of that page by 1.
            print("Hit :",i)
            cache[[k[0] for k in cache].index(i)][1] += 1 #increasing hits of requested page by 1.
        print(cache)
    print("\nCache List with first element representing page and second element representing number of hits:")
    print(cache)

def requestinput():
    """
    requestinput function is used to take the request from the user which is continuously aking for input
    until user press 0.
    """
    global request
    request = []
    i = int(input("Enter request or 0 to stop : "))
    while (i != 0):
        request.append(i)
        i = int(input("Enter request or 0 to stop : "))

def main():
    global cache
    cache = []
    #This loop runs the menu and thn calls the requested function from menu. This loop stops the programme 
    #when Q is pressed.
    while True:
        menu = input("\nPress 1 for FIFO, or 2 for LFU, or press Q to quit : ")
        print()
        if menu == "q" or menu == "Q":
            exit()
        if menu == "1":
            requestinput()
            fifo()
            cache.clear()
        elif menu == "2":
            requestinput()
            lfo()
            cache.clear()
        else:
            print("Enter valid input from menu")

if __name__ == "__main__":
    main()