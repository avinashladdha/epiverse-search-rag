# Age in Years of Individuals

```r
age(x, reference = Sys.Date(), exact = FALSE, na.rm = FALSE, ...)
```

## Arguments

- `x`: date(s), character (vectors) will be coerced with `as.POSIXlt()`
- `reference`: reference date(s) (default is today), character (vectors) will be coerced with `as.POSIXlt()`
- `exact`: a logical to indicate whether age calculation should be exact, i.e. with decimals. It divides the number of days of [year-to-date](https://en.wikipedia.org/wiki/Year-to-date) (YTD) of `x` by the number of days in the year of `reference` (either 365 or 366).
- `na.rm`: a logical to indicate whether missing values should be removed
- `...`: arguments passed on to `as.POSIXlt()`, such as `origin`

## Returns

An integer (no decimals) if `exact = FALSE`, a double (with decimals) otherwise

## Description

Calculates age in years based on a reference date, which is the system date at default.

## Details

Ages below 0 will be returned as `NA` with a warning. Ages above 120 will only give a warning.

This function vectorises over both `x` and `reference`, meaning that either can have a length of 1 while the other argument has a larger length.

## Examples

```r
# 10 random pre-Y2K birth dates
df <- data.frame(birth_date = as.Date("2000-01-01") - runif(10) * 25000)

# add ages
df$age <- age(df$birth_date)

# add exact ages
df$age_exact <- age(df$birth_date, exact = TRUE)

# add age at millenium switch
df$age_at_y2k <- age(df$birth_date, "2000-01-01")

df
```

## See Also

To split ages into groups, use the `age_groups()` function.



