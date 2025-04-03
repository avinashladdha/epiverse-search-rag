# wrapper for bootstrap relative efficiency confidence interval

```r
boot_re(
  pred_data,
  period.all,
  model_good,
  bench.all,
  type,
  truth = "CDC.data",
  l = 50,
  N = 10000,
  sim = "geom",
  conf = 0.95
)
```

## Arguments

- `pred_data`: A matrix that contains the truth vector and the predictions. It can be data.frame or xts object
- `period.all`: vector of the periods to evaluate relative efficiency
- `model_good`: The model to evaluate, must be in the column names of pred_data
- `bench.all`: vector of the models to compare to, must be in the column names of pred_data
- `type`: Must be one of "mse" (mean square error), "mape" (mean absolute percentage error), or "mae" (mean absolute error)
- `truth`: the column name of the truth
- `l`: stationary bootstrap mean block length
- `N`: number of bootstrap samples
- `sim`: simulation method, pass to boot::tsboot
- `conf`: confidence level

## Returns

A vector of point estimate and corresponding bootstrap confidence interval

## Description

This function is used to wrap the `bootstrap_relative_efficiency`, taking vectorized arguments.

## Examples

```r
GFT_xts = xts::xts(exp(matrix(rnorm(500), ncol=5)), order.by = Sys.Date() - (100:1))
names(GFT_xts) <- paste0("col", 1:ncol(GFT_xts))
names(GFT_xts)[1] <- "CDC.data"

boot_re(
  pred_data = GFT_xts,
  period.all = c(paste0(zoo::index(GFT_xts)[1], "/", zoo::index(GFT_xts)[50]),
                 paste0(zoo::index(GFT_xts)[51], "/", zoo::index(GFT_xts)[100])),
  model_good = "col2",
  bench.all = c("col3", "col4"),
  type = "mse",
  truth="CDC.data",
  l = 5,
  N = 20
)
```



