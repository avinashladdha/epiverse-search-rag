# Aggregate a contact matrix

```r
aggregate_contact_matrix(object, lookup_table, age_distr)
```

## Arguments

- `object`: data.frame; a contact matrix. See contact_matrix .
- `lookup_table`: data.frame; a user-defined data.frame which maps the sixteen 5-year age bands to a new set of age bands.
- `age_distr`: data.frame; the aggregated age distribution. See aggregate_contact_matrix .

## Returns

An object of class **data.frame**.

## Description

Function to aggregate a contact matrix according to user-defined age groups.

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

# Import the projected contact matrix for Greece:
conmat <- contact_matrix(country = "GRC")

# Aggregate the contact matrix:
aggr_cm <- aggregate_contact_matrix(conmat, lookup_table, aggr_age)

# Plot the contact matrix:
plot_contact_matrix(aggr_cm)
```



