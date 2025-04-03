# Distribution of the time between infection and death

```r
itd_distribution(
  ts_length,
  gamma_mean = 24.19231,
  gamma_cv = 0.3987261,
  gamma_shape = 6.29,
  gamma_rate = 0.26
)
```

## Arguments

- `ts_length`: integer; time from infection to death in days.
- `gamma_mean`: numeric; mean of a gamma distribution, for a given shape and rate. See also `GammaDist`.
- `gamma_cv`: numeric; coefficient of variation of a gamma distribution, for a given shape and rate. See also `GammaDist`.
- `gamma_shape`: numeric; shape parameter of a gamma distribution. See also `GammaDist`.
- `gamma_rate`: numeric; rate parameter of a gamma distribution. See also `GammaDist`.

## Returns

A vector of length **ts_length**.

## Description

Function to discretize the infection-to-death distribution

## Examples

```r
# Age-specific mortality/incidence count time series:
data(age_specific_mortality_counts)

# Infection-to-death distribution:
ditd <- itd_distribution(ts_length  = nrow(age_specific_mortality_counts),
                         gamma_mean = 24.19231,
                         gamma_cv   = 0.3987261)
```

## References

Flaxman et al (2020). Estimating the effects of non-pharmaceutical interventions on COVID-19 in Europe. Nature, 584, 257-261.



