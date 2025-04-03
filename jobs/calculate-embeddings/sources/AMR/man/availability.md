# Check Availability of Columns

```r
availability(tbl, width = NULL)
```

## Arguments

- `tbl`: a data.frame or list
- `width`: number of characters to present the visual availability - the default is filling the width of the console

## Returns

data.frame with column names of `tbl` as row names

## Description

Easy check for data availability of all columns in a data set. This makes it easy to get an idea of which antimicrobial combinations can be used for calculation with e.g. `susceptibility()` and `resistance()`.

## Details

The function returns a data.frame with columns `"resistant"` and `"visual_resistance"`. The values in that columns are calculated with `resistance()`.

## Examples

```r
availability(example_isolates)

if (require("dplyr")) {
  example_isolates %>%
    filter(mo == as.mo("Escherichia coli")) %>%
    select_if(is.sir) %>%
    availability()
}
```



