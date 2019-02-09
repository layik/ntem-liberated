NTEM dataset liberated from mdb
================

Scripts to librate NTEM mdb files.

stats19 did a great job, this could also do a similar job.

``` r
# list the files from source
# https://data.gov.uk/dataset/11bc7aaf-ddf6-4133-a91d-84e6f20a663e/national-trip-end-model-ntem
```

But...lets think of non R users too

-   R
-   bash
    -   Export the mdb database into csv files: Thanks to <https://stackoverflow.com/a/52709174>

    `mdb-tables -d ',' database.mdb | xargs -L1 -d',' -I{} bash -c 'mdb-export database.mdb "$1" >"$1".csv' -- {}`

-   python
    -   The name comes from this [blog](http://mazamascience.com/WorkingWithData/?p=168) post and included python scripts too.

too
