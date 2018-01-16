import os

#This function replaces key/values in dict in the input parameter, outputed to os.cwd + newFile
#Used for ApeShape
def modifyNames(inputFile):
  dict = {'>NC_018424.0' : 'Gorillagorilla' ,'>NC_000023.21' : 'Homosapiens' , '>NC_000023.22' : 'Homosapiens' , '>NC_000023.23' : 'Homosapiens' ,'>NW_003571057.2':'Homosapiens', '>NC_006486.4':'Homosapiens'}
  x = 0
  firstLine = True
  complete = False
  fnaName = ''
  prevFileName = ''
  newFileName = ''
  ext = ".fasta"
  newFile = "GS_" + str(inputFile.rsplit('/',1)[-1])
  print(os.getcwd())
  open(str(os.getcwd()) + "/" + str(newFile), 'w').close()
  with open(inputFile, 'r') as file:
    with open(str(os.getcwd()) + "/" + str(newFile), 'w') as file2:
      for line in file:
          if(str(line[0]) == ">"):
             if str(line.strip()) in dict:
               file2.write(str(dict[str(line.strip())]) + "\n")
             else:
               file2.write(str(line.strip()) + "\n")
               pass
          else:
            file2.write(line)
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
    modifyNames(listFiles[i])

spider()

