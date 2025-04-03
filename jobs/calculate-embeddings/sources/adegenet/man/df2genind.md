# Convert a data.frame of allele data to a genind object.

```r
df2genind(
  X,
  sep = NULL,
  ncode = NULL,
  ind.names = NULL,
  loc.names = NULL,
  pop = NULL,
  NA.char = "",
  ploidy = 2,
  type = c("codom", "PA"),
  strata = NULL,
  hierarchy = NULL,
  check.ploidy = getOption("adegenet.check.ploidy")
)
```

## Arguments

- `X`: a matrix or a data.frame containing allelle data only (see decription)
- `sep`: a character string separating alleles. See details.
- `ncode`: an optional integer giving the number of characters used for coding one genotype at one locus. If not provided, this is determined from data.
- `ind.names`: optinal, a vector giving the individuals names; if NULL, taken from rownames of X. If factor or numeric, vector is converted to character.
- `loc.names`: an optional character vector giving the markers names; if NULL, taken from colnames of X.
- `pop`: an optional factor giving the population of each individual.
- `NA.char`: a character string corresponding to missing allele (to be treated as NA)
- `ploidy`: an integer indicating the degree of ploidy of the genotypes.
- `type`: a character string indicating the type of marker: 'codom' stands for 'codominant' (e.g. microstallites, allozymes); 'PA' stands for 'presence/absence' markers (e.g. AFLP, RAPD).
- `strata`: an optional data frame that defines population stratifications for your samples. This is especially useful if you have a hierarchical or factorial sampling design.
- `hierarchy`: a hierarchical formula that explicitely defines hierarchical levels in your strata.
- `check.ploidy`: a boolean indicating if the ploidy should be checked (TRUE, default) or not (FALSE). Not checking the ploidy makes the import much faster, but might result in bugs/problems if the input file is misread or the ploidy is wrong. It is therefore advised to first import and check a subset of data to see if everything works as expected before setting this option to false.

## Returns

an object of the class genind for `df2genind`; a matrix of biallelic genotypes for `genind2df`

## Description

The function `df2genind` converts a data.frame (or a matrix) into a genind object. The data.frame must meet the following requirements:

 * genotypes are in row (one row per genotype)
 * markers/loci are in columns
 * each element is a string of characters coding alleles, ideally separated by a character string (argument `sep`); if no separator is used, the number of characters coding alleles must be indicated (argument `ncode`).

## Details

See `genind2df` to convert genind objects back to such a data.frame.

=== Details for the `sep` argument ===

this character is directly used in reguar expressions like `gsub`, and thus require some characters to be preceeded by double backslashes. For instance, "/" works but "|" must be coded as "\|".

## Examples

```r
## simple example
df <- data.frame(locusA=c("11","11","12","32"),
locusB=c(NA,"34","55","15"),locusC=c("22","22","21","22"))
row.names(df) <- .genlab("genotype",4)
df

obj <- df2genind(df, ploidy=2, ncode=1)
obj
tab(obj)


## converting a genind as data.frame
genind2df(obj)
genind2df(obj, sep="/")
```

## See Also

`genind2df`, `import2genind`, `read.genetix`, `read.fstat`, `read.structure`

## Author(s)

Thibaut Jombart t.jombart@imperial.ac.uk , Zhian N. Kamvar kamvarz@science.oregonstate.edu



