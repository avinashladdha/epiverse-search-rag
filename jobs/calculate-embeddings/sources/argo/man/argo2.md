# ARGO second step

```r
argo2(truth, argo1.p, argo.nat.p)
```

## Arguments

- `truth`: prediction target
- `argo1.p`: argo first step prediction
- `argo.nat.p`: argo national level prediction

## Description

Wrapper for ARGO second step. Best linear predictor / Bayesian posterior

## Examples

```r
truth <- xts::xts(exp(matrix(rnorm(180*10), ncol=10)), order.by = Sys.Date() - (180:1))
argo1.p <- xts::xts(exp(matrix(rnorm(180*10), ncol=10)), order.by = Sys.Date() - (180:1))
argo.nat.p <- xts::xts(exp(matrix(rnorm(180*10), ncol=10)), order.by = Sys.Date() - (180:1))
argo2result <- argo2(truth, argo1.p, argo.nat.p)
```

## References

Shaoyang Ning, Shihao Yang, S. C. Kou. Accurate Regional Influenza Epidemics Tracking Using Internet Search Data. Scientific Reports



