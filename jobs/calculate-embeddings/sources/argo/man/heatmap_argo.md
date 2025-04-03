# Heatmap plot of ARGO coefficients applied on CDC's ILI data

```r
heatmap_argo(argo_coef, lim = 0.1, na.grey = TRUE, scale = 1)
```

## Arguments

- `argo_coef`: The coefficient matrix
- `lim`: the limit to truncate for large coefficients for better presentation
- `na.grey`: whether to plot grey for NA values
- `scale`: margin scale

## Returns

a graph on the default plot window

## Description

Heatmap plot of ARGO coefficients applied on CDC's ILI data

## Examples

```r
cor_coef <- matrix(runif(100, -1, 1), ncol=10)
colnames(cor_coef) <- as.character(Sys.Date() - 10:1)
rownames(cor_coef) <- paste0("row", 1:10)
pdf(file.path(tempdir(), "heatmap_argo.pdf"), height=11,width=12)
heatmap_argo(cor_coef)
dev.off()
```



