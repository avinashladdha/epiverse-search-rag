UTF-8

# Genetic distances between populations

## Description

This function computes measures of genetic distances between populations using a `genpop` object.

Currently, five distances are available, some of which are euclidian (see details).

A non-euclidian distance can be transformed into an Euclidean one using `cailliez` in order to perform a Principal Coordinate Analysis `dudi.pco` (both functions in `ade4`).

The function `dist.genpop` is based on former `dist.genet` function of `ade4` package.

```r
dist.genpop(x, method = 1, diag = FALSE, upper = FALSE)
```

## Arguments

- `x`: a list of class `genpop`
- `method`: an integer between 1 and 5. See details
- `diag`: a logical value indicating whether the diagonal of the distance matrix should be printed by `print.dist`
- `upper`: a logical value indicating whether the upper triangle of the distance matrix should be printed by `print.dist`

## Details

Let A a table containing allelic frequencies with **t** populations (rows) and **m** alleles (columns).

Let `\nu` the number of loci. The locus **j** gets **m(j)** alleles. `m=\sum_{j=1}^{\nu} m(j)`

For the row **i** and the modality **k** of the variable **j**, notice the value `a_{ij}^k` (`1 \leq i \leq t`, `1 \leq j \leq \nu`, `1 \leq k \leq m(j)`) the value of the initial table.

`a_{ij}^+=\sum_{k=1}^{m(j)}a_{ij}^k` and `p_{ij}^k=\frac{a_{ij}^k}{a_{ij}^+}`

Let P the table of general term `p_{ij}^k`

`p_{ij}^+=\sum_{k=1}^{m(j)}p_{ij}^k=1`, `p_{i+}^+=\sum_{j=1}^{\nu}p_{ij}^+=\nu`, `p_{++}^+=\sum_{j=1}^{\nu}p_{i+}^+=t\nu`

The option `method` computes the distance matrices between populations using the frequencies `p_{ij}^k`.

1. Nei's distance (not Euclidean):

c("`D_1(a,b)=- \\ln(\\frac{\\sum_{k=1}^{\\nu} \\sum_{j=1}^{m(k)}\n`", "`p_{aj}^k p_{bj}^k}{\\sqrt{\\sum_{k=1}^{\\nu} \\sum_{j=1}^{m(k)}\n`", "`{(p_{aj}^k) }^2}\\sqrt{\\sum_{k=1}^{\\nu} \\sum_{j=1}^{m(k)}\n`", "`{(p_{bj}^k)}^2}})`")

2. Angular distance or Edwards' distance (Euclidean):

c("`D_2(a,b)=\\sqrt{1-\\frac{1}{\\nu} \\sum_{k=1}^{\\nu}\n`", "`\\sum_{j=1}^{m(k)} \\sqrt{p_{aj}^k  p_{bj}^k}}`")

3. Coancestrality coefficient or Reynolds' distance (Eucledian):

c("`D_3(a,b)=\\sqrt{\\frac{\\sum_{k=1}^{\\nu}\n`", "`\\sum_{j=1}^{m(k)}{(p_{aj}^k - p_{bj}^k)}^2}{2 \\sum_{k=1}^{\\nu} (1-\n`", "`\\sum_{j=1}^{m(k)}p_{aj}^k p_{bj}^k)}}`")

4. Classical Euclidean distance or Rogers' distance (Eucledian):

c("`D_4(a,b)=\\frac{1}{\\nu} \\sum_{k=1}^{\\nu} \\sqrt{\\frac{1}{2}\n`", "`\\sum_{j=1}^{m(k)}{(p_{aj}^k - p_{bj}^k)}^2}`")

5. Absolute genetics distance or Provesti 's distance (not Euclidean):

c("`D_5(a,b)=\\frac{1}{2{\\nu}} \\sum_{k=1}^{\\nu} \\sum_{j=1}^{m(k)}\n`", "`|p_{aj}^k - p_{bj}^k|`")

## Returns

returns a distance matrix of class `dist` between the rows of the data frame

## References

To complete informations about distances:

Distance 1:

Nei, M. (1972) Genetic distances between populations. **American Naturalist**, 106 , 283--292.

Nei M. (1978) Estimation of average heterozygosity and genetic distance from a small number of individuals. **Genetics**, 23 , 341--369.

Avise, J. C. (1994) Molecular markers, natural history and evolution. Chapman & Hall, London.

Distance 2:

Edwards, A.W.F. (1971) Distance between populations on the basis of gene frequencies. **Biometrics**, 27 , 873--881.

Cavalli-Sforza L.L. and Edwards A.W.F. (1967) Phylogenetic analysis: models and estimation procedures. **Evolution**, 32 , 550--570.

Hartl, D.L. and Clark, A.G. (1989) Principles of population genetics. Sinauer Associates, Sunderland, Massachussetts (p. 303).

Distance 3:

Reynolds, J. B., B. S. Weir, and C. C. Cockerham. (1983) Estimation of the coancestry coefficient: basis for a short-term genetic distance. **Genetics**, 105 , 767--779.

Distance 4:

Rogers, J.S. (1972) Measures of genetic similarity and genetic distances. **Studies in Genetics**, Univ. Texas Publ., 7213 , 145--153.

Avise, J. C. (1994) Molecular markers, natural history and evolution. Chapman & Hall, London.

Distance 5:

Prevosti A. (1974) La distancia genetica entre poblaciones. **Miscellanea Alcobe**, 68 , 109--118.

Prevosti A., Ocaña J. and Alonso G. (1975) Distances between populations of Drosophila subobscura, based on chromosome arrangements frequencies. **Theoretical and Applied Genetics**, 45 , 231--241.

For more information on dissimilarity indexes:

Gower J. and Legendre P. (1986) Metric and Euclidean properties of dissimilarity coefficients. **Journal of Classification**, 3 , 5--48

Legendre P. and Legendre L. (1998) **Numerical Ecology**, Elsevier Science B.V. 20, pp274--288.

 

## Author(s)

Thibaut Jombart t.jombart@imperial.ac.uk

Former dist.genet code by Daniel Chessel chessel@biomserv.univ-lyon1.fr

and documentation by Anne B. Dufour dufour@biomserv.univ-lyon1.fr

## See Also

`cailliez`,`dudi.pco`

## Examples

```r
## Not run:

data(microsatt)
obj <- as.genpop(microsatt$tab)

listDist <- lapply(1:5, function(i) cailliez(dist.genpop(obj,met=i)))
for(i in 1:5) {attr(listDist[[i]],"Labels") <- popNames(obj)}
listPco <- lapply(listDist, dudi.pco,scannf=FALSE)

par(mfrow=c(2,3))
for(i in 1:5) {scatter(listPco[[i]],sub=paste("Dist:", i))}
## End(Not run)
```



