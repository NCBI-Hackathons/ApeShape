# ApeShape
### A Project endeavors to find the ancestral states of genetics variants provided by database.

## Please cite our work -- here is the ICMJE Standard Citation:
(Fill when we get a DOI)
## Awesome Logo
![alt text](https://i.pinimg.com/736x/c7/9e/77/c79e77061058fe2f14bb22225be441a1.jpg)
### You can make a free DOI with zenodo <link>
## Intro statement
This pipeline finds ancestral states of each polymorphic site in clinVar (Test case).
The project can be used to study the evolution of genome since it is able to find the ancestral states of a large number of genetic variants. 
## What's the problem?
Finding the ancestral states of a large number of genetic variants (provided by database or user).
## Why should we solve it?
The results provided by this project will give researchers a large number of ancestral states data which helps them with their researches.
# Workflow
![alt text](https://github.com/NCBI-Hackathons/PrimateAncestralAlleles/blob/master/workflow.png?raw=true)
# How to use <this software>
  ## Data Preparation
The data_preparation.R can gather chromosome numbers and SNP postions from NCBI .vcf file. The .bed file generated should be feeded to https://genome.ucsc.edu/cgi-bin/hgCustom. In the website, you should click "Add custom track". The page will be directed to a place where you can upload your file.
After your file is uploaded, a page like this:


![alt text](https://github.com/NCBI-Hackathons/PrimateAncestralAlleles/blob/master/Customtrack.png?raw=true) 


should appear, and you can select it and choose view in tabe browser.
Now you will enter this page


![alt text](https://github.com/NCBI-Hackathons/PrimateAncestralAlleles/blob/master/tablebrowser.png?raw=true)


In 'Output format section choose 'sequence', and type in a file name in 'output file' section. Click 'get output' and a file will start to download. This is the sequence file prepared for BLAST.

  
  
  
  
  
  
![alt tag](https://socalhack2018.slack.com/messages/C8H3T34BG/details/)
  
