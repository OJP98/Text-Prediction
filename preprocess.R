library(wordcloud)
library(tm)
library(ngram)
library(RWeka)
library(readtext)
library(quanteda)


twitter <- readtext("./en_US.twitter.txt")
news <- readtext("./en_US.news.txt")
blogs <- readtext("./en_US.blogs.txt")

corpus_twitter <- corpus(twitter)
summary(corpus_twitter, 5)


