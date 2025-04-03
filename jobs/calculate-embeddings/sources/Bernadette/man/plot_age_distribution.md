# Bar plot of the age distribution

```r
plot_age_distribution(x)
```

## Arguments

- `x`: data.frame; the age distribution matrix. See age_distribution and aggregate_age_distribution .

## Returns

A ggplot object that can be further customized using the `ggplot2` package.

## Description

Bar plot of the age distribution

## Examples

```r
# Import the age distribution for Greece in 2020:
age_distr <- age_distribution(country = "Greece", year = 2020)

plot_age_distribution(age_distr)

# Lookup table:
lookup_table <- data.frame(Initial = age_distr$AgeGrp,
                           Mapping = c(rep("0-39",  8),
                                       rep("40-64", 5),
                                       rep("65+"  , 3)))

# Aggregate the age distribution table:
aggr_age <- aggregate_age_distribution(age_distr, lookup_table)

# Plot the aggregated age distribution matrix:
plot_age_distribution(aggr_age)
```

## References

United Nations, Department of Economic and Social Affairs, Population Division (2019). World Population Prospects 2019, Online Edition. Rev. 1.



