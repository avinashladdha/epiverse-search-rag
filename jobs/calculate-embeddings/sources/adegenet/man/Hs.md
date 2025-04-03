# Expected heterozygosity (Hs)

```r
Hs(x, pop = NULL)
```

## Arguments

- `x`: a genind or genpop object.
- `pop`: only used if x is a genind ; an optional factor to be used as population; if not provided, pop(x) is used.

## Returns

a vector of Hs values (one value per population)

## Description

This function computes the expected heterozygosity (Hs) within populations of a genpop object. This function is available for codominant markers (`@type="codom"`) only. Hs is commonly used for measuring within population genetic diversity (and as such, it still has sense when computed from haploid data).

## Details

Let **m(k)** be the number of alleles of locus **k**, with a total of **K** loci. We note `f_i` the allele frequency of allele **i** in a given population. Then, `Hs` is given for a given population by:

`\frac{1}{K} \sum_{k=1}^K (1 - \sum_{i=1}^{m(k)} f_i^2)`

## Examples

```r
## Not run:

data(nancycats)
Hs(genind2genpop(nancycats))
## End(Not run)
```

## See Also

`Hs.test` to test differences in Hs between two groups

## Author(s)

Thibaut Jombart t.jombart@imperial.ac.uk



