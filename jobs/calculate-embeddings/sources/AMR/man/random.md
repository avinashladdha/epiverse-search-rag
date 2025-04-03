# Random MIC Values/Disk Zones/SIR Generation

```r
random_mic(size = NULL, mo = NULL, ab = NULL, ...)

random_disk(size = NULL, mo = NULL, ab = NULL, ...)

random_sir(size = NULL, prob_SIR = c(0.33, 0.33, 0.33), ...)
```

## Arguments

- `size`: desired size of the returned vector. If used in a data.frame call or `dplyr` verb, will get the current (group) size if left blank.
- `mo`: any character that can be coerced to a valid microorganism code with `as.mo()`
- `ab`: any character that can be coerced to a valid antimicrobial drug code with `as.ab()`
- `...`: ignored, only in place to allow future extensions
- `prob_SIR`: a vector of length 3: the probabilities for "S" (1st value), "I" (2nd value) and "R" (3rd value)

## Returns

class `mic` for `random_mic()` (see `as.mic()`) and class `disk` for `random_disk()` (see `as.disk()`)

## Description

These functions can be used for generating random MIC values and disk diffusion diameters, for AMR data analysis practice. By providing a microorganism and antimicrobial drug, the generated results will reflect reality as much as possible.

## Details

The base function `sample()` is used for generating values.

Generated values are based on the EUCAST 2023 guideline as implemented in the clinical_breakpoints data set. To create specific generated values per bug or drug, set the `mo` and/or `ab` argument.

## Examples

```r
random_mic(25)
random_disk(25)
random_sir(25)


# make the random generation more realistic by setting a bug and/or drug:
random_mic(25, "Klebsiella pneumoniae") # range 0.0625-64
random_mic(25, "Klebsiella pneumoniae", "meropenem") # range 0.0625-16
random_mic(25, "Streptococcus pneumoniae", "meropenem") # range 0.0625-4

random_disk(25, "Klebsiella pneumoniae") # range 8-50
random_disk(25, "Klebsiella pneumoniae", "ampicillin") # range 11-17
random_disk(25, "Streptococcus pneumoniae", "ampicillin") # range 12-27
```



