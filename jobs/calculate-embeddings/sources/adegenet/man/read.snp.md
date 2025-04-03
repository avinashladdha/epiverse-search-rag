# Reading Single Nucleotide Polymorphism data

```r
read.snp(
  file,
  quiet = FALSE,
  chunkSize = 1000,
  parallel = FALSE,
  n.cores = NULL,
  ...
)
```

## Arguments

- `file`: a character string giving the path to the file to convert, with the extension ".snp".
- `quiet`: logical stating whether a conversion messages should be printed (TRUE,default) or not (FALSE).
- `chunkSize`: an integer indicating the number of genomes to be read at a time; larger values require more RAM but decrease the time needed to read the data.
- `parallel`: a logical indicating whether multiple cores -if available- should be used for the computations (TRUE, default), or not (FALSE); requires the package `parallel` to be installed (see details).
- `n.cores`: if `parallel` is TRUE, the number of cores to be used in the computations; if NULL, then the maximum number of cores available on the computer is used.
- ``...``: other arguments to be passed to other functions - currently not used.

## Returns

an object of the class `"genlight"`

## Description

The function `read.snp` reads a SNP data file with extension '.snp' and converts it into a genlight object. This format is devoted to handle biallelic SNP only, but can accommodate massive datasets such as complete genomes with considerably less memory than other formats.

## Details

The function reads data by chunks of a few genomes (minimum 1, no maximum) at a time, which allows one to read massive datasets with negligible RAM requirements (albeit at a cost of computational time). The argument `chunkSize` indicates the number of genomes read at a time. Increasing this value decreases the computational time required to read data in, while increasing memory requirements.

A description of the .snp format is provided in an example file distributed with adegenet (see example below).

=== The .snp format ===

Details of the .snp format can be found in the example file distributed with adegenet (see below), or on the adegenet website (type `adegenetWeb()` in R).

## Examples

```r
## Not run:

## show the example file ##
## this is the path to the file:
system.file("files/exampleSnpDat.snp",package="adegenet")

## show its content:
file.show(system.file("files/exampleSnpDat.snp",package="adegenet"))


## read the file
obj <-
read.snp(system.file("files/exampleSnpDat.snp",package="adegenet"), chunk=2)
obj
as.matrix(obj)
ploidy(obj)
alleles(obj)
locNames(obj)
## End(Not run)
```

## See Also

- `?genlight` for a description of the class `"genlight"`.

- `read.PLINK`: read SNPs in PLINK's '.raw' format.

- `fasta2genlight`: extract SNPs from alignments with fasta format.

- `df2genind`: convert any multiallelic markers into adegenet `"genlight"`.

- `import2genind`: read multiallelic markers from various software into adegenet.

## Author(s)

Thibaut Jombart t.jombart@imperial.ac.uk



