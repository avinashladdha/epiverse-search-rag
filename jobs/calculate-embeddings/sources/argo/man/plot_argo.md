# Time series plot of ARGO applied on CDC's ILI data

```r
plot_argo(GFT_xts, GC_GT_cut_date, model_names, legend_names, zoom_periods)
```

## Arguments

- `GFT_xts`: dataframe with all predicted values
- `GC_GT_cut_date`: cutting date for switching datasets
- `model_names`: name of predicting models
- `legend_names`: legend for predicting models
- `zoom_periods`: vector of periods to zoom into

## Returns

a graph on the default plot window

## Description

This function is used to reproduce the ARGO plot.

## Examples

```r
GFT_xts = xts::xts(exp(matrix(rnorm(1000), ncol=5)), order.by = Sys.Date() - (200:1))
names(GFT_xts) <- paste0("col", 1:ncol(GFT_xts))
names(GFT_xts)[1] <- "CDC.data"
zoom_periods = c()
for (i in 0:5){
  zoom_periods = c(
    zoom_periods,
    paste0(zoo::index(GFT_xts)[i*30+1], "/", zoo::index(GFT_xts)[i*30+30])
  )
}
plot_argo(
  GFT_xts = GFT_xts,
  GC_GT_cut_date = zoo::index(GFT_xts)[50],
  model_names = colnames(GFT_xts)[-1],
  legend_names = paste0(colnames(GFT_xts)[-1], "legend"),
  zoom_periods = zoom_periods
)
```



