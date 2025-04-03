UTF-8

# Read large DNA alignments into R

## Description

The function `fasta2DNAbin` reads alignments with the fasta format (extensions ".fasta", ".fas", or ".fa"), and outputs a `DNAbin` object (the efficient DNA representation from the ape package). The output contains either the full alignments, or only SNPs. This implementation is designed for memory-efficiency, and can read in larger datasets than Ape's `read.dna`.

The function reads data by chunks of a few genomes (minimum 1, no maximum) at a time, which allows one to read massive datasets with negligible RAM requirements (albeit at a cost of computational time). The argument `chunkSize` indicates the number of genomes read at a time. Increasing this value decreases the computational time required to read data in, while increasing memory requirements.

```r
fasta2DNAbin(file, quiet=FALSE, chunkSize=10, snpOnly=FALSE)
```

## Arguments

- `file`: a character string giving the path to the file to convert, with the extension ".fa", ".fas", or ".fasta".
    
    Can also be a connection (which will be opened for reading if necessary, and if so `close`d (and hence destroyed) at the end of the function call).
- `quiet`: a logical stating whether a conversion messages should be printed (FALSE, default) or not (TRUE).
- `chunkSize`: an integer indicating the number of genomes to be read at a time; larger values require more RAM but decrease the time needed to read the data.
- `snpOnly`: a logical indicating whether SNPs only should be returned.

## Returns

an object of the class `DNAbin`

## See Also

- `?DNAbin` for a description of the class `DNAbin`.

- `read.snp`: read SNPs in adegenet's '.snp' format.

- `read.PLINK`: read SNPs in PLINK's '.raw' format.

- `df2genind`: convert any multiallelic markers into adegenet genind .

- `import2genind`: read multiallelic markers from various software into adegenet.

## Author(s)

Thibaut Jombart t.jombart@imperial.ac.uk

## Examples

```r
## Not run:

## show the example file ##
## this is the path to the file:
myPath <- system.file("files/usflu.fasta",package="adegenet")
myPath

## read the file
obj <- fasta2DNAbin(myPath, chunk=10) # process 10 sequences at a time
obj
## End(Not run)
```



