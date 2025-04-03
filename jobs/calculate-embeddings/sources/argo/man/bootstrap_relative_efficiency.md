# bootstrap relative efficiency confidence interval

```r
bootstrap_relative_efficiency(
  pred_data,
  model_good,
  model_bench,
  l = 50,
  N = 10000,
  truth = "CDC.data",
  sim = "geom",
  conf = 0.95,
  type = c("mse", "mape", "mae", "mspe", "rmse", "rmspe")
)
```

## Arguments

- `pred_data`: A matrix that contains the truth vector and the predictions. It can be data.frame or xts object
- `model_good`: The model to evaluate, must be in the column names of pred_data
- `model_bench`: The model to compare to, must be in the column names of pred_data
- `l`: stationary bootstrap mean block length
- `N`: number of bootstrap samples
- `truth`: the column name of the truth
- `sim`: simulation method, pass to boot::tsboot
- `conf`: confidence level
- `type`: Must be one of "mse" (mean square error), "mape" (mean absolute percentage error), or "mae" (mean absolute error)

## Returns

A vector of point estimate and corresponding bootstrap confidence interval

## Description

This function is used to reproduce the ARGO bootstrap confidence interval

## Examples

```r
GFT_xts = xts::xts(exp(matrix(rnorm(1000), ncol=5)), order.by = Sys.Date() - (200:1))
names(GFT_xts) <- paste0("col", 1:ncol(GFT_xts))
names(GFT_xts)[1] <- "CDC.data"
bootstrap_relative_efficiency(
  pred_data = GFT_xts,
  model_good = "col2",
  model_bench = "col3",
  truth="CDC.data",
  N = 100
)
```



