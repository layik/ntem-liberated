library(rvest)
library(stringr)
u = paste0(
  "https://data.gov.uk/dataset/",
  "11bc7aaf-ddf6-4133-a91d-84e6f20a663e/",
  "national-trip-end-model-ntem")
page = read_html(u)
#'
r = page %>%
  html_nodes("a") %>%       # find all links
  html_attr("href") %>%     # get the url
  str_subset("\\.zip")
r = r[!grepl(x = r, pattern = "document")]
r[1]
#'
dr = c(length(r))
for(i in 1:length(r)) {
  dr[i] = sub("http://data.dft.gov.uk.s3.amazonaws.com/road-accidents-safety-data/",
              "", URLdecode(r[i]))
  dr[i] = sub("http://assets.dft.gov.uk.s3.amazonaws.com/tempro/version7.2/",
              "", dr[i])
}

