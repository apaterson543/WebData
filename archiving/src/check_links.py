
"""
Ensure that all links are unique
"""
file = open('../output/unique_urls.txt', 'r')

links = file.readlines()
flag = False
for link in links:
    count = 0
    for other in links:
        print("\ncomparing " + link +" and "+other+'\n') 
        if link == other:
            count += 1
        if count >1:    
            print('not unique')
            flag = True
            break
    if flag:
        break
if flag == False:
    print('ALL GOOD!')
