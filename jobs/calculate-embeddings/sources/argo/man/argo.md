# Construct ARGO object

```r
argo(
  data,
  exogen = xts::xts(NULL),
  N_lag = 1:52,
  N_training = 104,
  alpha = 1,
  use_all_previous = FALSE,
  mc.cores = 1,
  schedule = list()
)
```

## Arguments

- `data`: response variable as xts, last element can be NA. If the response is later revised, it should be an xts that resembles upper triangular square matrix, with each column being the data available as of date of column name
- `exogen`: exogenous predictors, default is NULL
- `N_lag`: vector of the AR model lags used, if NULL then no AR lags will be used
- `N_training`: number of training points, if `use_all_previous` is true, this is the least number of training points required
- `alpha`: penalty between lasso and ridge, alpha=1 represents lasso, alpha=0 represents ridge, alpha=NA represents no penalty
- `use_all_previous`: boolean variable indicating whether to use "all available data" (when `TRUE`) or "a sliding window" (when `FALSE`) for training
- `mc.cores`: number of cores to compute argo in parallel
- `schedule`: list to specify prediction schedule. Default to have `y_gap` as 1, and `forecast` as 0, i.e., nowcasting with past week ILI available from CDC.

## Returns

A list of following named objects

 * `pred` An xts object with the same index as input, which contains historical nowcast estimation
 * `coef` A matrix contains historical coefficient values of the predictors.
 * `parm` Parameter values passed to argo function.
 * `penalfac` the value of lambda ratio selected by cross-validation, NULL if `lamid` is NULL or has only one level.
 * `penalregion` the lambda ratios that has a cross validation error within one standard error of minimum cross validation error

## Description

Wrapper for ARGO. The real work horse is glmnet package and/or linear model.

## Details

This function takes the time series and exogenous variables (optional) as input, and produces out-of-sample prediction for each time point.

## Examples

```r
GFT_xts <- xts::xts(exp(matrix(rnorm(180), ncol=1)), order.by = Sys.Date() - (180:1))
randomx <- xts::xts(exp(matrix(rnorm(180*100), ncol=100)), order.by = Sys.Date() - (180:1))

argo_result1 <- argo(GFT_xts)
argo_result2 <- argo(GFT_xts, exogen = randomx)
```

## References

Yang, S., Santillana, M., & Kou, S. C. (2015). Accurate estimation of influenza epidemics using Google search data via ARGO. Proceedings of the National Academy of Sciences. <doi:10.1073/pnas.1515373112>.



