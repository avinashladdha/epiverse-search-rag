# Kurtosis of the Sample

```r
kurtosis(x, na.rm = FALSE, excess = FALSE)

## Default S3 method:
kurtosis(x, na.rm = FALSE, excess = FALSE)

## S3 method for class 'matrix'
kurtosis(x, na.rm = FALSE, excess = FALSE)

## S3 method for class 'data.frame'
kurtosis(x, na.rm = FALSE, excess = FALSE)
```

## Arguments

- `x`: a vector of values, a matrix or a data.frame
- `na.rm`: a logical to indicate whether `NA` values should be stripped before the computation proceeds
- `excess`: a logical to indicate whether the **excess kurtosis** should be returned, defined as the kurtosis minus 3.

## Description

Kurtosis is a measure of the "tailedness" of the probability distribution of a real-valued random variable. A normal distribution has a kurtosis of 3 and a excess kurtosis of 0.

## Examples

```r
kurtosis(rnorm(10000))
kurtosis(rnorm(10000), excess = TRUE)
```

## See Also

`skewness()`



