class ReadFile():
    def __init__(self, file):
        try:
            # read all the lines of file with path ./resources/file.csv
            fileHandler = open("../resources/" + file, 'r')
            self.lines = fileHandler.readlines()
            fileHandler.close()
        except:
            print("Faild to read File : ", str(file))

    def getLines(self):
        return self.lines

class WriteToFile():
    def __init__(self, file):
        try:
            self.fileHandler = open("../resources/" + file, 'a')
        except:
            print("Faild to read File : ", str(file))

    def writeALine(self, line):
        self.fileHandler.write(line+"\r")
    def __exit__(self, *args):
        self.fileHandler.close()


class ReadCosts():
    def __init__(self):
        self.data = ReadFile("InterviewData_Cost.csv").getLines()
        self.headers = self.data[0]
        self.data = self.data[1:]


class ReadRevenues():
    def __init__(self):
        self.data = ReadFile("InterviewData_Rev.csv").getLines()
        self.headers = self.data[0]
        self.data = self.data[1:]


class ReadActivity():
    def __init__(self):
        self.data = ReadFile("InterviewData_Activity.csv").getLines()
        self.headers = self.data[0]
        self.data = self.data[1:]


class ReadParsing():
    def __init__(self):
        self.data = ReadFile("InterviewData_Parsing.csv").getLines()
        self.headers = self.data[0]
        self.data = self.data[1:]


def problem1():
    print("starting solving problem 1 and savind answer to ../resources/problem1.csv")

def problem2():
    print("starting solving problem 1 and savind answer to ../resources/problem2.csv")

def problem3():
    print("starting solving problem 1 and savind answer to ../resources/problem3.csv")

def problem4():
    print("starting solving problem 1 and savind answer to ../resources/problem4.csv")

def problem5():
    print("starting solving problem 1 and savind answer to ../resources/problem5.csv")

def problem6():
    print("starting solving problem 1 and savind answer to ../resources/problem6.csv")

'''
rev=ReadRevenues()
print(rev.headers.split(","))
print(rev.data[0].split(","))
write=WriteToFile("test.csv")
write.writeALine("date,source_id,cost,revenue")
write.writeALine("8/1/14,PA0368,5717")
'''