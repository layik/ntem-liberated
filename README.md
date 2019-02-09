NTEM dataset liberated from mdb
================

Scripts to librate NTEM mdb files using [mdbtools](https://github.com/brianb/mdbtools).

stats19 did a great job, this could also do a similar job. Let's think of non-R users too.

``` r
# list the files from source
# https://data.gov.uk/dataset/11bc7aaf-ddf6-4133-a91d-84e6f20a663e/national-trip-end-model-ntem

source("scrape.R")
```

    ## Loading required package: xml2

``` r
dr
```

    ##  [1] "SW_280217_72.zip"       "LON_280217_72.zip"     
    ##  [3] "NW_280217_72.zip"       "SCOTLAND_280217_72.zip"
    ##  [5] "SE_280217_72.zip"       "WALES_280217_72.zip"   
    ##  [7] "WM_280217_72.zip"       "YH_280217_72.zip"      
    ##  [9] "EAST_280217_72.zip"     "EM_280217_72.zip"      
    ## [11] "NE_280217_72.zip"

``` r
#' example of unzipping to mdb
#' unzip to exe
#' then unzip to mdb
exe = sub(pattern = ".zip", replacement = ".exe", dr[1])
mdb = sub(pattern = ".zip", replacement = ".mdb", dr[1])

if(!file.exists(dr[1]))
  download.file(r[1], dr[1])
if(!file.exists(exe))
  unzip(dr[1])
if(!file.exists(mdb))
  system(paste0("unzip -o ", exe))
```

-   R
-   bash
    -   Export the mdb database into csv files: Thanks to <https://stackoverflow.com/a/52709174>

    `mdb-tables -d ',' database.mdb | xargs -L1 -d',' -I{} bash -c 'mdb-export database.mdb "$1" >"$1".csv' -- {}`

-   python
    -   The name comes from this [blog](http://mazamascience.com/WorkingWithData/?p=168) post and included python scripts too.

too
