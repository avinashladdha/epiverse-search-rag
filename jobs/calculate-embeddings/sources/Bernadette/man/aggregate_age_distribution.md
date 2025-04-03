# Aggregate the age distribution matrix

```r
aggregate_age_distribution(x, lookup_table)
```

## Arguments

- `x`: data.frame; an age distribution matrix. See age_distribution .
- `lookup_table`: data.frame; a user-defined dataframe which maps the sixteen 5-year age bands to a new set of age bands.

## Returns

An object of class **data.frame** that contains the aggregated age distribution.

## Description

Function to aggregate the age distribution according to user-defined age groups.

## Examples

```r
# Import the age distribution for Greece in 2020:
age_distr <- age_distribution(country = "Greece", year = 2020)

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

Prem, K., van Zandvoort, K., Klepac, P. et al (2020). Projecting contact matrices in 177 geographical regions: an update and comparison with empirical data for the COVID-19 era. medRxiv 2020.07.22.20159772; doi: https://doi.org/10.1101/2020.07.22.20159772



