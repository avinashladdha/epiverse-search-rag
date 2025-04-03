# performance summary of ARGO applied on CDC's ILI data

```r
summary_argo(
  GFT_xts,
  model_names,
  legend_names,
  periods,
  whole_period = "2009-03/2015-10"
)
```

## Arguments

- `GFT_xts`: dataframe with all predicted values
- `model_names`: name of predicting models
- `legend_names`: legend for predicting models
- `periods`: vector of periods to zoom into
- `whole_period`: the whole period duration

## Returns

A list of summary tables for the input periods, including RMSE, MAE, MAPE, corr

## Description

performance summary of ARGO applied on CDC's ILI data

## Examples

```r
GFT_xts = xts::xts(exp(matrix(rnorm(1000), ncol=10)), order.by = Sys.Date() - (100:1))
names(GFT_xts) <- paste0("col", 1:10)
names(GFT_xts)[1] <- "CDC.data"
summary_argo(
  GFT_xts = GFT_xts,
  model_names = colnames(GFT_xts)[-1],
  legend_names = paste0(colnames(GFT_xts)[-1], "legend"),
  periods = c(paste0(zoo::index(GFT_xts)[1], "/", zoo::index(GFT_xts)[49]),
              paste0(zoo::index(GFT_xts)[50], "/", zoo::index(GFT_xts)[100])),
  whole_period="2009-03/"
)
```

## References

Yang, S., Santillana, M., & Kou, S. C. (2015). Accurate estimation of influenza epidemics using Google search data via ARGO. Proceedings of the National Academy of Sciences. <doi:10.1073/pnas.1515373112>. Shaoyang Ning, Shihao Yang, S. C. Kou. Accurate Regional Influenza Epidemics Tracking Using Internet Search Data. Scientific Reports



