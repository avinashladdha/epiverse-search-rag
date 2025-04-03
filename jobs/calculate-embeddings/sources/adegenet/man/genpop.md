UTF-8

# adegenet formal class (S4) for allele counts in populations

## Description

An object of class `genpop` contain alleles counts for several loci.

It contains several components (see 'slots' section).

Such object is obtained using `genind2genpop` which converts individuals genotypes of known population into a `genpop` object. Note that the function `summary` of a `genpop` object returns a list of components. Note that as in other S4 classes, slots are accessed using @ instead of $.

## Slots

- **`tab`:**: matrix of alleles counts for each combinaison of population (in rows) and alleles (in columns).
- **`loc.fac`:**: locus factor for the columns of `tab`
- **`loc.n.all`:**: integer vector giving the number of alleles per locus
- **`all.names`:**: list having one component per locus, each containing a character vector of alleles names
- **`call`:**: the matched call
- **`ploidy`:**: an integer indicating the degree of ploidy of the genotypes. Beware: 2 is not an integer, but as.integer(2) is.
- **`type`:**: a character string indicating the type of marker: 'codom' stands for 'codominant' (e.g. microstallites, allozymes); 'PA' stands for 'presence/absence' (e.g. AFLP).
- **`other`:**: (optional) a list containing other information

## Extends

Class `"gen"`, directly. Class `"popInfo"`, directly.

## Methods

- **names**: `signature(x = "genpop")`: give the names of the components of a genpop object
- **print**: `signature(x = "genpop")`: prints a genpop object
- **show**: `signature(object = "genpop")`: shows a genpop object (same as print)
- **summary**: `signature(object = "genpop")`: summarizes a genpop object, invisibly returning its content or suppress printing of auxiliary information by specifying `verbose = FALSE`

## See Also

`as.genpop`, `is.genpop`,`makefreq`, `genind`, `import2genind`, `read.genetix`, `read.genepop`, `read.fstat`

## Author(s)

Thibaut Jombart t.jombart@imperial.ac.uk

## Examples

```r
obj1 <- import2genind(system.file("files/nancycats.gen",
package="adegenet"))
obj1


obj2 <- genind2genpop(obj1)
obj2

## Not run:

data(microsatt)
# use as.genpop to convert convenient count tab to genpop
obj3 <- as.genpop(microsatt$tab)
obj3

all(obj3@tab==microsatt$tab)

# perform a correspondance analysis
obj4 <- genind2genpop(obj1,missing="chi2")
ca1 <- dudi.coa(as.data.frame(obj4@tab),scannf=FALSE)
s.label(ca1$li,sub="Correspondance Analysis",csub=2)
add.scatter.eig(ca1$eig,2,xax=1,yax=2,posi="top")
## End(Not run)
```



