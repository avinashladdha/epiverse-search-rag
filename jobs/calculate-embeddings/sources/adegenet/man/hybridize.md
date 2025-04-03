# Function hybridize takes two genind in inputs and generates hybrids individuals having one parent in both objects.

```r
hybridize(
  x1,
  x2,
  n,
  pop = "hybrid",
  res.type = c("genind", "df", "STRUCTURE"),
  file = NULL,
  quiet = FALSE,
  sep = "/",
  hyb.label = "h"
)
```

## Arguments

- `x1`: a genind object
- `x2`: a genind object
- `n`: an integer giving the number of hybrids requested
- `pop`: a character string giving naming the population of the created hybrids.
- `res.type`: a character giving the type of output requested. Must be "genind" (default), "df" (i.e. data.frame like in `genind2df`), or "STRUCTURE" to generate a .str file readable by STRUCTURE (in which case the 'file' must be supplied). See 'details' for STRUCTURE output.
- `file`: a character giving the name of the file to be written when 'res.type' is "STRUCTURE"; if NULL, a the created file is of the form "hybrids_[the current date].str".
- `quiet`: a logical specifying whether the writing to a file (when 'res.type' is "STRUCTURE") should be announced (FALSE, default) or not (TRUE).
- `sep`: a character used to separate two alleles
- `hyb.label`: a character string used to construct the hybrids labels; by default, "h", which gives labels: "h01", "h02", "h03",...

## Returns

A genind object (by default), or a data.frame of alleles (res.type="df"). No R output if res.type="STRUCTURE" (results written to the specified file).

## Description

The function `hybridize` performs hybridization between two set of genotypes stored in genind objects (referred as the "2 populations"). Allelic frequencies are derived for each population, and then gametes are sampled following a multinomial distribution.

## Details

The result consists in a set of 'n' genotypes, with different possible outputs (see 'res.type' argument).

If the output is a STRUCTURE file, this file will have the following caracteristics:

- file contains the genotypes of the parents, and then the genotypes of hybrids

- the first column identifies genotypes

- the second column identifies the population (1 and 2 for parents x1 and x2; 3 for hybrids)

- the first line contains the names of the markers

- one row = one genotype (onerowperind will be true)

- missing values coded by "-9" (the software's default)

## Examples

```r
## Not run:

## Let's make some cattle hybrids
data(microbov)

## first, isolate each breed
temp <- seppop(microbov)
names(temp)
salers <- temp$Salers
zebu <- temp$Zebu

## let's make some... Zeblers
zebler <- hybridize(salers, zebu, n=40,
                    pop="Zebler")


## now let's merge all data into a single genind
newDat <- repool(microbov, zebler)

## make a correspondance analysis
## and see where hybrids are placed
X <- genind2genpop(newDat, quiet=TRUE)
coa1 <- dudi.coa(tab(X),scannf=FALSE,nf=3)
s.label(coa1$li)
add.scatter.eig(coa1$eig,2,1,2)
## End(Not run)
```

## See Also

`seploc`, `seppop`, `repool`

## Author(s)

Thibaut Jombart t.jombart@imperial.ac.uk



