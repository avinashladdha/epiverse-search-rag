UTF-8

# Likelihood-based estimation of inbreeding

## Description

The function `inbreeding` estimates the inbreeding coefficient of an individuals (F) by computing its likelihood function. It can return either the density of probability of F, or a sample of F values from this distribution. This operation is performed for all the individuals of a genind object. Any ploidy greater than 1 is acceptable.

```r
inbreeding(x, pop = NULL, truenames = TRUE, 
           res.type = c("sample", "function", "estimate"), N = 200, M = N * 10)
```

## Arguments

- `x`: an object of class genind .
- `pop`: a factor giving the 'population' of each individual. If NULL, pop is seeked from `pop(x)`. Note that the term population refers in fact to any grouping of individuals'.
- `truenames`: a logical indicating whether true names should be used (TRUE, default) instead of generic labels (FALSE); used if res.type is "matrix".
- `res.type`: a character string matching "sample", "function", or "estimate" specifying whether the output should be a function giving the density of probability of F values ("function"), the maximum likelihood estimate of F from this distribution ("estimate"), or a sample of F values taken from this distribution ("sample", default).
- `N`: an integer indicating the size of the sample to be taken from the distribution of F values.
- `M`: an integer indicating the number of different F values to be used to generate the sample. Values larger than N are recommended to avoid poor sampling of the distribution.

## Returns

A named list with one component for each individual, each of which is a function or a vector of sampled F values (see `res.type` argument).

## See Also

`Hs`: computation of expected heterozygosity.

## Details

Let `F` denote the inbreeding coefficient, defined as the probability for an individual to inherit two identical alleles from a single ancestor.

Let `p_i` refer to the frequency of allele `i` in the population. Let `h` be an variable which equates 1 if the individual is homozygote, and 0 otherwise. For one locus, the probability of being homozygote is computed as:

 ` F + (1-F) \sum_i p_i^2`

The probability of being heterozygote is: `1 - (F + (1-F) \sum_i p_i^2)`

The likelihood of a genotype is defined as the probability of being the observed state (homozygote or heterozygote). In the case of multilocus genotypes, log-likelihood are summed over the loci.

## Author(s)

Thibaut Jombart t.jombart@imperial.ac.uk

Zhian N. Kamvar

## Examples

```r
## Not run:

## cattle breed microsatellite data
data(microbov)

## isolate Lagunaire breed
lagun <- seppop(microbov)$Lagunaire

## estimate inbreeding - return sample of F values
Fsamp <- inbreeding(lagun, N=30)

## plot the first 10 results
invisible(sapply(Fsamp[1:10], function(e) plot(density(e), xlab="F",
xlim=c(0,1), main="Density of the sampled F values")))

## compute means for all individuals
Fmean=sapply(Fsamp, mean)
hist(Fmean, col="orange", xlab="mean value of F",
main="Distribution of mean F across individuals")

## estimate inbreeding - return proba density functions
Fdens <- inbreeding(lagun, res.type="function")

## view function for the first individual
Fdens[[1]]

## plot the first 10 functions
invisible(sapply(Fdens[1:10], plot, ylab="Density",
main="Density of probability of F values"))

## estimate inbreeding - return maximum likelihood estimates
Fest <- inbreeding(lagun, res.type = "estimate")
mostInbred <- which.max(Fest)
plot(Fdens[[mostInbred]], ylab = "Density", xlab = "F",
     main = paste("Probability density of F values\nfor", names(mostInbred)))
abline(v = Fest[mostInbred], col = "red", lty = 2)
legend("topright", legend = "MLE", col = "red", lty = 2)

## note that estimates and average samples are likely to be different.
plot(Fest, ylab = "F", col = "blue",
     main = "comparison of MLE and average sample estimates of F")
points(Fmean, pch = 2, col = "red")
arrows(x0 = 1:length(Fest), y0 = Fest, 
       y1 = Fmean, x1 = 1:length(Fest), length = 0.125)
legend("topleft", legend = c("estimate", "sample"), col = c("blue", "red"),
       pch = c(1, 2), title = "res.type")
## End(Not run)
```



