# Skewness of the Sample

```r
skewness(x, na.rm = FALSE)

## Default S3 method:
skewness(x, na.rm = FALSE)

## S3 method for class 'matrix'
skewness(x, na.rm = FALSE)

## S3 method for class 'data.frame'
skewness(x, na.rm = FALSE)
```

## Arguments

- `x`: a vector of values, a matrix or a data.frame
- `na.rm`: a logical value indicating whether `NA` values should be stripped before the computation proceeds

## Description

Skewness is a measure of the asymmetry of the probability distribution of a real-valued random variable about its mean.

When negative ('left-skewed'): the left tail is longer; the mass of the distribution is concentrated on the right of a histogram. When positive ('right-skewed'): the right tail is longer; the mass of the distribution is concentrated on the left of a histogram. A normal distribution has a skewness of 0.

## Examples

```r
skewness(runif(1000))
```

## See Also

`kurtosis()`



