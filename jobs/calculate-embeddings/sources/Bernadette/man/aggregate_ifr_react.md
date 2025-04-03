# Aggregate the Infection Fatality Ratio

```r
aggregate_ifr_react(x, user_AgeGrp, data_cases)
```

## Arguments

- `x`: data.frame; an age distribution matrix. See age_distribution .
- `user_AgeGrp`: vector; a user-defined vector which maps the four age groups considered in REACT-2 to a new set of age groups.
- `data_cases`: data.frame; time series dataset containing the age-stratified infection counts. See age_specific_infection_counts .

## Returns

A list of two data frames that contains the aggregated IFR estimates.

## Description

Function to aggregate the age-specific Infection Fatality Ratio (IFR) estimates reported by the REACT-2 large-scale community study of SARS-CoV-2 seroprevalence in England according to user-defined age groups.

## Examples

```r
# Import the age distribution for Greece in 2020:
age_distr <- age_distribution(country = "Greece", year = 2020)

age_mapping <- c(rep("0-39",  8),
                 rep("40-64", 5),
                 rep("65+",   3))

data(age_specific_infection_counts)

# Aggregate the IFR:
aggr_age_ifr <- aggregate_ifr_react(age_distr, age_mapping, age_specific_infection_counts)
```

## References

Ward, H., Atchison, C., Whitaker, M. et al. (2021). SARS-CoV-2 antibody prevalence in England following the first peak of the pandemic. Nature Communications 12, 905



