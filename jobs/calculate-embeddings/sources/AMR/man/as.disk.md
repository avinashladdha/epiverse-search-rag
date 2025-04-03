 data

# Transform Input to Disk Diffusion Diameters

## Format

An object of class `disk` (inherits from `integer`) of length 1.

```r
as.disk(x, na.rm = FALSE)

NA_disk_

is.disk(x)
```

## Arguments

- `x`: vector
- `na.rm`: a logical indicating whether missing values should be removed

## Returns

An integer with additional class `disk`

## Description

This transforms a vector to a new class `disk`, which is a disk diffusion growth zone size (around an antibiotic disk) in millimetres between 6 and 50.

## Details

Interpret disk values as SIR values with `as.sir()`. It supports guidelines from EUCAST and CLSI.

Disk diffusion growth zone sizes must be between 6 and 50 millimetres. Values higher than 50 but lower than 100 will be maximised to 50. All others input values outside the 6-50 range will return `NA`. `NA_disk_` is a missing value of the new `disk` class.

## Examples

```r
# transform existing disk zones to the `disk` class (using base R)
df <- data.frame(
  microorganism = "Escherichia coli",
  AMP = 20,
  CIP = 14,
  GEN = 18,
  TOB = 16
)
df[, 2:5] <- lapply(df[, 2:5], as.disk)
str(df)


# transforming is easier with dplyr:
if (require("dplyr")) {
  df %>% mutate(across(AMP:TOB, as.disk))
}


# interpret disk values, see ?as.sir
as.sir(
  x = as.disk(18),
  mo = "Strep pneu", # `mo` will be coerced with as.mo()
  ab = "ampicillin", # and `ab` with as.ab()
  guideline = "EUCAST"
)

# interpret whole data set, pretend to be all from urinary tract infections:
as.sir(df, uti = TRUE)
```

## See Also

`as.sir()`



