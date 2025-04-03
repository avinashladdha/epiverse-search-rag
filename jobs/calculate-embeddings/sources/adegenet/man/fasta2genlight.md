UTF-8

# Extract Single Nucleotide Polymorphism (SNPs) from alignments

## Description

The function `fasta2genlight` reads alignments with the fasta format (extensions ".fasta", ".fas", or ".fa"), extracts the binary SNPs, and converts the output into a genlight object.

The function reads data by chunks of a few genomes (minimum 1, no maximum) at a time, which allows one to read massive datasets with negligible RAM requirements (albeit at a cost of computational time). The argument `chunkSize` indicates the number of genomes read at a time. Increasing this value decreases the computational time required to read data in, while increasing memory requirements.

Multiple cores can be used to decrease the overall computational time on parallel architectures (needs the package `parallel`).

```r
fasta2genlight(file, quiet = FALSE, chunkSize = 1000, saveNbAlleles = FALSE,
               parallel = FALSE, n.cores = NULL, ...)
```

## Arguments

- `file`: a character string giving the path to the file to convert, with the extension ".fa", ".fas", or ".fasta".
- `quiet`: logical stating whether a conversion messages should be printed (FALSE,default) or not (TRUE).
- `chunkSize`: an integer indicating the number of genomes to be read at a time; larger values require more RAM but decrease the time needed to read the data.
- `saveNbAlleles`: a logical indicating whether the number of alleles for each loci in the original alignment should be saved in the `other` slot (TRUE), or not (FALSE, default). In large genomes, this takes some space but allows for tracking SNPs with more than 2 alleles, lost during the conversion.
- `parallel`: a logical indicating whether multiple cores -if available- should be used for the computations (TRUE, default), or not (FALSE); requires the package `parallel` to be installed (see details).
- `n.cores`: if `parallel` is TRUE, the number of cores to be used in the computations; if NULL, then the maximum number of cores available on the computer is used.
- ``...``: other arguments to be passed to other functions - currently not used.

## Details

 === Using multiple cores ===

Most recent machines have one or several processors with multiple cores. R processes usually use one single core. The package `parallel` allows for parallelizing some computations on multiple cores, which decreases drastically computational time.

To use this functionality, you need to have the last version of the `parallel` package installed.

## Returns

an object of the class genlight

## See Also

- `?genlight` for a description of the class genlight .

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
obj <- fasta2genlight(myPath, chunk=10) # process 10 sequences at a time
obj

## look at extracted information
position(obj)
alleles(obj)
locNames(obj)

## plot positions of polymorphic sites
temp <- density(position(obj), bw=10)
plot(temp, xlab="Position in the alignment", lwd=2, main="Location of the SNPs")
points(position(obj), rep(0, nLoc(obj)), pch="|", col="red")
## End(Not run)
```



