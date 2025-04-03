# Test differences in expected heterozygosity (Hs)

```r
Hs.test(x, y, n.sim = 999, alter = c("two-sided", "greater", "less"))
```

## Arguments

- `x`: a genind object.
- `y`: a genind object.
- `n.sim`: the number of permutations to be used to generate the reference distribution.
- `alter`: a character string indicating the alternative hypothesis

## Returns

an object of the class randtest

## Description

This procedure permits to test if two groups have significant differences in expected heterozygosity (Hs). The test statistic used is simply the difference in Hs between the two groups 'x' and 'y':

## Details

`Hs(x) - Hs(y)`

Individuals are randomly permuted between groups to obtain a reference distribution of the test statistics.

## Examples

```r
## Not run:

data(microbov)
Hs(microbov)
test <- Hs.test(microbov[pop="Borgou"],
                microbov[pop="Lagunaire"],
                n.sim=499)
test
plot(test)
## End(Not run)
```

## See Also

`Hs` to compute Hs for different populations; `as.randtest` for the class of Monte Carlo tests.

## Author(s)

Thibaut Jombart t.jombart@imperial.ac.uk



