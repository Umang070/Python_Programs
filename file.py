# with open("index.html","r") as webpage:
#     with open("output.txt","a") as wf:
#         for line in webpage.readlines():
#             if '<a href= ' in line:
#                 pos = line.find("<a href=")
#                 first_quote = line.find(" \" ",pos)
#                 sec_quote = line.find(" \" ",first_quote+1)#b'caz after some string we find sec "
#                 url = line[first_quote+1:sec_quote]
#                  wf.write(url + "\n") not work if many url in one line...

# ----------------SOLUTION----------

# with open("index.html","r") as webpage:
#      with open("output.txt","a") as wf:
#          page = webpage.read()
#          line_exist = True
#          while line_exist:
#              pos = page.find("<a href=")
#              if pos == -1: #not find pos of <a href
#                 line_exist = False
#              else:
#                  first_quote = line.find(" \" ",pos)
#                  sec_quote = line.find(" \" ",first_quote+1)#b'caz after some string we find sec "
#                  url = line[first_quote+1:sec_quote]
# #                  wf.write(url + "\n") #our problem is solve......

# with open("story.txt","r",encoding="utf-8") as f:  # for emojis files
#     print(f.encoding)
#     print(f.read())

# if u read big.........big file...........-----------

with open("file.txt","r") as rf:
    data = rf.read(10)
    while len(data) > 0:
        print(data)
        data = rf.read(10)  #only 10 charchter runn
