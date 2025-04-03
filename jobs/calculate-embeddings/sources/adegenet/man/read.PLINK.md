# Reading PLINK Single Nucleotide Polymorphism data

```r
extract.PLINKmap(file, x = NULL)

read.PLINK(
  file,
  map.file = NULL,
  quiet = FALSE,
  chunkSize = 1000,
  parallel = FALSE,
  n.cores = NULL,
  ...
)
```

## Arguments

- `file`: for `read.PLINK` a character string giving the path to the file to convert, with the extension ".raw"; for `extract.PLINKmap`, a character string giving the path to a file with extension ".map".
- `x`: an optional object of the class `"genlight"`, in which the information read is stored; if provided, information is matched against the names of the loci in `x`, as returned by `locNames(x)`; if not provided, a list of two components is returned, containing chromosome and position information.
- `map.file`: an optional character string indicating the path to a ".map" file, which contains information about the SNPs (chromosome, position). If provided, this information is processed by `extract.PLINKmap` and stored in the `@other` slot.
- `quiet`: logical stating whether a conversion messages should be printed (TRUE,default) or not (FALSE).
- `chunkSize`: an integer indicating the number of genomes to be read at a time; larger values require more RAM but decrease the time needed to read the data.
- `parallel`: a logical indicating whether multiple cores -if available- should be used for the computations (TRUE, default), or not (FALSE); requires the package `parallel` to be installed (see details).
- `n.cores`: if `parallel` is TRUE, the number of cores to be used in the computations; if NULL, then the maximum number of cores available on the computer is used.
- ``...``: other arguments to be passed to other functions - currently not used.

## Returns

- read.PLINK: an object of the class `"genlight"`

- extract.PLINKmap: if a `"genlight"` is provided as argument `x`, this object incorporating the new information about SNPs in the `@other` slot (with new components 'chromosome' and 'position'); otherwise, a list with two components containing chromosome and position information.

## Description

The function `read.PLINK` reads a data file exported by the PLINK software with extension '.raw' and converts it into a `"genlight"` object. Optionally, information about SNPs can be read from a ".map" file, either by specifying the argument `map.file` in `read.PLINK`, or using `extract.PLINKmap` to add information to an existing `"genlight"` object.

## Details

The function reads data by chunks of several genomes (minimum 1, no maximum) at a time, which allows one to read massive datasets with negligible RAM requirements (albeit at a cost of computational time). The argument `chunkSize` indicates the number of genomes read at a time. Increasing this value decreases the computational time required to read data in, while increasing memory requirements.

See details for the documentation about how to export data using PLINK to the '.raw' format.

=== Exporting data from PLINK ===

Data need to be exported from PLINK using the option "--recodeA" (and NOT "--recodeAD"). The PLINK command should therefore look like: `plink --file data --recodeA`. For more information on this topic, please look at this webpage: [http://zzz.bwh.harvard.edu/plink/](http://zzz.bwh.harvard.edu/plink/)

## See Also

- `?genlight` for a description of the class `"genlight"`.

- `read.snp`: read SNPs in adegenet's '.snp' format.

- `fasta2genlight`: extract SNPs from alignments with fasta format.

- other import function in adegenet: `import2genind`, `df2genind`, `read.genetix` `read.fstat`, `read.structure`, `read.genepop`.

- another function `read.plink` is available in the package `snpMatrix`.

## Author(s)

Thibaut Jombart t.jombart@imperial.ac.uk



