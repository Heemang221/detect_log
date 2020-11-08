import glob
import re

keyword = str("!!! Found Hacker")

with open('C:/Users/USER/Desktop/log1102/newoutput.txt', 'w') as w:

    p = re.compile(keyword)

    total_counter = 0
    files = glob.glob(r'C:/Users/USER/Desktop/log1102/logfile*.txt')
    for i in files:
        counter = 0
        with open(i, 'r') as f:
            for x, y in enumerate(f.readlines(),1):
                m = p.findall(y)
                if m:
                    counter += 1
                    print('File : %s \n [ %d ] \n Line Searching : %s \n' %(i[30:],x,m))
                    #write
                    w.write(y)
                    #
        print('\n File : %s \n Frequency : %d \n' %(i[30:], counter))
        w.write('\n File : %s \n Frequency : %d \n' %(i[30:], counter))
        total_counter += counter
    print('\n Total Frequency : %d' %total_counter)
    w.write('\nTotal Frequency : %d' %total_counter)

