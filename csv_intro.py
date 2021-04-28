# from csv import reader 

# with open("first.csv","r") as f:
#     csv_reader = reader(f) #iterator
#     next(csv_reader)        # for not print heading
#     for row in csv_reader:
#         print(row)

# ----------another solutionn ---------------

# from csv import DictReader  #ordered dict...........
 
# with open ("first.csv","r") as f:
#     csv_reader = DictReader(f)      #f,delimiter =" | "
#     for row in csv_reader:
#         print(row["name"])

# -------------write in csv ----------
# from csv import writer
# with open("first.csv","a",newline = "") as aw:
        # csv_writer = writer(aw)
        # csv_writer.writerow(["subject","marks"])
        # csv_writer.writerow(["maths",89])
        
        # csv_writer.writerows([["country","capital"],["india","delhi"],["france","paris"]])

#-----------write with dictwrite -----------
from csv import DictWriter
with open("first.csv","a",newline = "") as aw:
        csv_writer = DictWriter(aw,fieldnames=["name","age"]) #for specify header...........
        csv_writer.writeheader()
        # csv_writer.writerow({})
        csv_writer.writerows([
            {"name" : "umang","age"  : 19},
            {"name" : "chintu","age" : 18}
                            ])