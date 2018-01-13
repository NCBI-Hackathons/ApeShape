#!/usr/local/bin/R

ApeShape_withprint <- function(infile, inTree){
args <- commandArgs(trailingOnly=TRUE)
  
library(phangorn)
library(ape)
  
tree <- read.tree(file= args[2])
seq <- read.FASTA(file= args[1])
phyDat <- phyDat(seq,type="DNA")
treePML <- pml(tree,phyDat)
anc <- ancestral.pml(treePML)
baseIndex <- which.max(anc$'7')

if (baseIndex == 1) {
  base = 'A'}
  else if (baseIndex == 2){
    base = "C"}
  else if (baseIndex == 3){
    base = "G"}
  else if (baseIndex == 4){
    base = "T"
  }

return(list(args[], base))

}

ApeShape_withprint(inData, inTree)

