import os
#This function prints the 76th character underneath the >Name
#For example
#>NC00001
#A
#>NC00002
#C
#where A and C are the 76th characters
#change ext fasta into txt
def seventySix(inputFile):
  x = 0
  firstLine = True
  complete = False
  fnaName = ''
  prevFileName = ''
  newFileName = ''
  newFile = "76_" + str(inputFile.rsplit('/',1)[-1])
  #print(newFile)
  firstLine = False
  #print(os.getcwd())
  open(str(os.getcwd()) + "/" + str(newFile), 'w').close()
  with open(inputFile, 'r') as file:
    with open(str(os.getcwd()) + "/" + str(newFile), 'w') as file2:
      for line in file:
          if(str(line[0]) == ">"):
             file2.write(line)
             firstLine = True
          else:
            if(firstLine is True):
              if(line[0].isalpha()):
                #print(str(line[75]))
                #0...75 where 75 is 76th character
                if(len(line) > 150):
                  file2.write(str(line[75]) + "\n")
            firstLine = False
      else:
        #file2.write(line)
        pass
    file.close()
    file2.close()

def spider():
  ext = ".fasta"
  listFiles = []
  for root, dir, files in os.walk(os.getcwd(), topdown=True):
    for currentFile in files:
      if currentFile.endswith(ext):
        print(currentFile)
        listFiles.append(str(currentFile))
  #print(listFiles)
  for i in range(len(listFiles)):
    #print(listFiles[i])
    seventySix(listFiles[i])

spider()




