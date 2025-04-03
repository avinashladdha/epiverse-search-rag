# Importing data from several softwares to a genind object

```r
import2genind(file, quiet = FALSE, ...)
```

## Arguments

- `file`: a character string giving the path to the file to convert, with the appropriate extension.
- `quiet`: logical stating whether a conversion message must be printed (TRUE,default) or not (FALSE).
- ``...``: other arguments passed to the appropriate 'read' function (currently passed to `read.structure`)

## Returns

an object of the class `genind`

## Description

Their are several ways to import genotype data to a genind

object: i) from a data.frame with a given format (see `df2genind`), ii) from a file with a recognized extension, or iii) from an alignement of sequences (see `DNAbin2genind`).

## Details

The function `import2genind` detects the extension of the file given in argument and seeks for an appropriate import function to create a `genind` object.

Current recognized formats are :

- GENETIX files (.gtx)

- Genepop files (.gen)

- Fstat files (.dat)

- STRUCTURE files (.str or .stru)

Beware: same data in different formats are not expected to produce exactly the same `genind` objects.

For instance, conversions made by GENETIX to Fstat may change the the sorting of the genotypes; GENETIX stores individual names whereas Fstat does not; Genepop chooses a sample's name from the name of its last genotype; etc.

## Examples

```r
import2genind(system.file("files/nancycats.gtx",
package="adegenet"))

import2genind(system.file("files/nancycats.dat",
package="adegenet"))

import2genind(system.file("files/nancycats.gen",
package="adegenet"))

import2genind(system.file("files/nancycats.str",
package="adegenet"), onerowperind=FALSE, n.ind=237, n.loc=9, col.lab=1, col.pop=2, ask=FALSE)
```

## References

Belkhir K., Borsa P., Chikhi L., Raufaste N. & Bonhomme F. (1996-2004) GENETIX 4.05, logiciel sous Windows TM pour la genetique des populations. Laboratoire Genome, Populations, Interactions, CNRS UMR 5000, Universite de Montpellier II, Montpellier (France).

Pritchard, J.; Stephens, M. & Donnelly, P. (2000) Inference of population structure using multilocus genotype data. **Genetics**, 155 : 945-959

Raymond M. & Rousset F, (1995). GENEPOP (version 1.2): population genetics software for exact tests and ecumenicism. **J. Heredity**, 86 :248-249

Fstat (version 2.9.3). Software by Jerome Goudet. http://www2.unil.ch/popgen/softwares/fstat.htm

Excoffier L. & Heckel G.(2006) Computer programs for population genetics data analysis: a survival guide **Nature**, 7 : 745-758

## See Also

`import2genind`, `read.genetix`, `read.fstat`, `read.structure`, `read.genepop`

## Author(s)

Thibaut Jombart t.jombart@imperial.ac.uk



