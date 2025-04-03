 data

utf-8

# Microsatellites genotypes of 335 chamois (Rupicapra rupicapra) from the Bauges mountains (France)

## Format

`rupica` is a genind object with 3 supplementary components inside the `@other` slot:

- **xy**: a matrix containing the spatial coordinates of the genotypes.
- **mnt**: a raster map of elevation, with the `asc` format from the `adehabitat` package.
- **showBauges**: a function to display the map of elevation with an appropriate legend (use `showBauges()`).

## Source

Daniel Maillard, 'Office National de la Chasse et de la Faune Sauvage' (ONCFS), France.

## Description

This data set contains the genotypes of 335 chamois (**Rupicapra rupicapra**) from the Bauges mountains, in France. No prior clustering about individuals is known. Each genotype is georeferenced. These data also contain a raster map of elevation of the sampling area.

## Examples

```r
data(rupica)
rupica


## Not run:

required_packages <- require(adehabitat) &&
  require(adespatial) &&
  require(spdep)
if (required_packages) {

## see the sampling area
showBauges <- rupica$other$showBauges
showBauges()
points(rupica$other$xy,col="red")

## perform a sPCA
spca1 <- spca(rupica,type=5,d1=0,d2=2300,plot=FALSE,scannf=FALSE,nfposi=2,nfnega=0)
barplot(spca1$eig,col=rep(c("black","grey"),c(2,100)),main="sPCA eigenvalues")
screeplot(spca1,main="sPCA eigenvalues: decomposition")

## data visualization
showBauges(,labcex=1)
s.value(spca1$xy,spca1$ls[,1],add.p=TRUE,csize=.5)
add.scatter.eig(spca1$eig,1,1,1,posi="topleft",sub="Eigenvalues")

showBauges(,labcex=1)
s.value(spca1$xy,spca1$ls[,2],add.p=TRUE,csize=.5)
add.scatter.eig(spca1$eig,2,2,2,posi="topleft",sub="Eigenvalues")

rupica$other$showBauges()
colorplot(spca1$xy,spca1$li,cex=1.5,add.plot=TRUE)

## global and local tests
Gtest <- global.rtest(rupica@tab,spca1$lw,nperm=999)
Gtest
plot(Gtest)
Ltest <- local.rtest(rupica@tab,spca1$lw,nperm=999)
Ltest
plot(Ltest)
}
## End(Not run)
```

## References

Cassar S (2008) Organisation spatiale de la variabilité génétique et phénotypique a l'échelle du paysage: le cas du chamois et du chevreuil, en milieu de montagne. PhD Thesis. University Claude Bernard - Lyon 1, France.

Cassar S, Jombart T, Loison A, Pontier D, Dufour A-B, Jullien J-M, Chevrier T, Maillard D. Spatial genetic structure of Alpine chamois (**Rupicapra rupicapra**): a consequence of landscape features and social factors? submitted to **Molecular Ecology**.



