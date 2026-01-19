# import pdb
# how to write a file and save it

# method 1 --> create a file and save it 
# try:

#     file = open("file.txt", "w")
#     file.write("Hello Suraj, welcome to file handling!!!")
#     file.close()
# except Exception as e:
#     print(f"which error if found :{e}")
# mthod 2 -- create a file and save it

# how to read content from file

# with open("file.txt", "r") as file1:
#     # content = file1.readline()  # read one line  at a time
#     # print(f"your file data is:{content}")
#     contet_lines = file1.readlines()
#     # content1 = file1.readline
#     print(f"read_all lines:{contet_lines}")

# Append (add more content without deleting old data)


def read_log():
    with open("app2.log" , "r") as log_read:
        return log_read.readlines()
        # print(log_read.readlines())
        # print(type(log))


def analyze_log(lines):

    # Dictionary to store log count
    log_count = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }
    for line in lines:
        if "INFO" in line:
            log_count.update({"INFO": log_count["INFO"]+1})
        
        elif "WARNING" in line:
            log_count.update({"WARNING": log_count["WARNING"]+1})
        
        elif "ERROR" in line:
            log_count.update({"ERROR": log_count["ERROR"]+1})
        else:
            pass
        
    return log_count 

lines = read_log()
counts = analyze_log(lines)
print("log counts are:", counts)