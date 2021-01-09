import os

# ten_link = "ten_link" + str(count)
search_string = 'coronavirus'
number_of_files_containing_term = 0
top_ten_links = ['','','','','','','','','','']
top_ten_counts = [0,0,0,0,0,0,0,0,0,0]
file_number = 0;
for file_number in range(1000):
    try:
        text_to_check = ''
        filename = "./io_text_resources/Cleaner/slimmed_text"+str(file_number)+".txt"

        with open(filename, 'r') as file:
            text_to_check = file.readlines()[2]

        count = text_to_check.count(search_string)
        if count >= 1:
            number_of_files_containing_term += 1
        file_number+=1
        # print(count)

        for i in range(len(top_ten_links)):
            if count > top_ten_counts[i]:
                top_ten_counts[i] = count
                top_ten_links[i] = filename
                break

    except:
        print(filename+ "not found")

top_ten_file_number = 0;
for link in top_ten_links:
    path = './io_text_resources/TopTen/top_ten' + str(top_ten_file_number) + '.txt'
    # file = '../io_text_resources/TopTen/top'
    # top_ten_file = open(path, 'w')
    with open(path, 'a') as top_ten_file:
        with open(link,'r') as top:
            top_ten_file.write(top.readline() + '\n')
            top_ten_file.writelines(top.readlines())
            top_ten_file.write('\n'+str(top_ten_counts[top_ten_file_number]))

    top_ten_file_number +=1
    # print(top_ten_links[i])
    # print(top_ten_counts[i])

with open('io_text_resources/TopTen/number_of_files_containing_term.txt','w') as file:
    file.write(str(number_of_files_containing_term))