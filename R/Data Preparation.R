#This code works for .vcf file from NCBI#
raw_data=as.matrix(read.csv(file = 'ApeShape',header = T))
#Change the .vcf to .csv if you have a .vcf file from NCBI#
chromosome_number=as.matrix(paste('chr',raw_data[,1],sep = ''))
Position=as.matrix(raw_data[,2],ncol=1)
Start_Position=Position[,1]-75
#75 can be changed to any number you like. But it is highly recommended that the 
#number should not be less than 50 since BLAST will not do a good alignment if length 
#of sequence which is shorter than 100.
End_Position=Position[,1]+75
BED_FILE=as.matrix(cbind(chromosome_number,Start_Position,End_Position))
write.table(BED_FILE,'Enter_your_file_name_do_not_change_the_suffix.bed',sep = '\t',quote = F)
#from here the .bed file is ready