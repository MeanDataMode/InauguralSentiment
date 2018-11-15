setwd("C:/Users/Tony/Desktop/ada-master-master/sentiment/")

library(ggplot2)
library(scales)
library(dplyr)
library(readr)

d <- read_tsv("inaugural_scores.txt")

ggplot(d,
       aes(x=word,y=score)) + 
  geom_line() + 
  theme_bw() + 
  scale_x_continuous(label=comma) + 
  labs(x="Word Position in Inaugurations,
       y="Running Sentiment Score",
       title="Sentiment of Inaugural\nOver the Course of the Speech") + 
  stat_smooth(se=F,col="red")



