# Prior distributions and options

```r
normal(location = 0, scale = NULL)

student_t(df = 1, location = 0, scale = NULL)

cauchy(location = 0, scale = NULL)

gamma(shape = 2, rate = 1)

exponential(rate = 1)
```

## Arguments

- `location`: Prior location. In most cases, this is the prior mean, but for `cauchy` (which is equivalent to `student_t` with `df=1`), the mean does not exist and `location` is the prior median. The default value is `0`.
- `scale`: Prior scale. The default depends on the family (see Details ).
- `df`: Degrees of freedom.
- `shape`: Prior shape for the gamma distribution. Defaults to `2`.
- `rate`: Prior rate for the exponential distribution. Defaults to `1`. For the exponential distribution, the rate parameter is the **reciprocal** of the mean.

## Returns

A named list to be used internally by the `Bernadette` model fitting functions.

## Description

The functions described on this page are used to specify the prior-related arguments of the modeling functions in the `Bernadette` package.

The default priors used in the `Bernadette` modeling functions are intended to be **weakly informative**. For many applications the defaults will perform well, but prudent use of more informative priors is encouraged. Uniform prior distributions are possible (e.g. by setting `stan_igbm`'s `prior` argument to `NULL`) but, unless the data is very strong, they are not recommended and are **not**

non-informative, giving the same probability mass to implausible values as plausible ones.

## Details

The details depend on the family of the prior being used:

### Student t family

Family members:

 * `normal(location, scale)`
 * `student_t(df, location, scale)`
 * `cauchy(location, scale)`

As the degrees of freedom approaches infinity, the Student t distribution approaches the normal distribution and if the degrees of freedom are one, then the Student t distribution is the Cauchy distribution. If `scale` is not specified it will default to `2.5`.

## Examples

```r
# Age-specific mortality/incidence count time series:
# Age-specific mortality/incidence count time series:
data(age_specific_mortality_counts)
data(age_specific_infection_counts)

# Import the age distribution for Greece in 2020:
age_distr <- age_distribution(country = "Greece", year = 2020)

# Lookup table:
lookup_table <- data.frame(Initial = age_distr$AgeGrp,
                          Mapping = c(rep("0-39",  8),
                                      rep("40-64", 5),
                                      rep("65+"  , 3)))

# Aggregate the age distribution table:
aggr_age <- aggregate_age_distribution(age_distr, lookup_table)

# Import the projected contact matrix for Greece:
conmat <- contact_matrix(country = "GRC")

# Aggregate the contact matrix:
aggr_cm <- aggregate_contact_matrix(conmat, lookup_table, aggr_age)

# Aggregate the IFR:
ifr_mapping <- c(rep("0-39", 8), rep("40-64", 5), rep("65+", 3))

aggr_age_ifr <- aggregate_ifr_react(age_distr, ifr_mapping, age_specific_infection_counts)

# Infection-to-death distribution:
ditd <- itd_distribution(ts_length  = nrow(age_specific_mortality_counts),
                         gamma_mean = 24.19231,
                         gamma_cv   = 0.3987261)

# Can assign priors to names:
N05      <- normal(0, 5)
Gamma22  <- gamma(2,2)
igbm_fit <- stan_igbm(y_data                      = age_specific_mortality_counts,
                      contact_matrix              = aggr_cm,
                      age_distribution_population = aggr_age,
                      age_specific_ifr            = aggr_age_ifr[[3]],
                      itd_distr                   = ditd,
                      likelihood_variance_type    = "quadratic",
                      prior_volatility            = N05,
                      prior_nb_dispersion         = Gamma22,
                      algorithm_inference         = "optimizing")
```

## See Also

The vignette for the `Bernadette` package discusses the use of some of the supported prior distributions.



