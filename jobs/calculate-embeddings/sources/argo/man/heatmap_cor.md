# Heatmap plot of correlation matrix

```r
heatmap_cor(cor_heat, lim = 1)
```

## Arguments

- `cor_heat`: The coefficient matrix to draw heatmap
- `lim`: the limit to truncate for large coefficients for better presentation

## Returns

a graph on the default plot window

## Description

Heatmap plot of correlation matrix

## Examples

```r
cor_coef <- matrix(runif(100, -1, 1), ncol=10)
colnames(cor_coef) <- paste0("col", 1:10)
rownames(cor_coef) <- paste0("row", 1:10)
heatmap_cor(cor_coef)
```



