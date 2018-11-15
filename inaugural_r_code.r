library(ggplot2)
library(scales)
library(dplyr)
library(readr)
library(ggthemes)

d <- read_tsv("inaugural_scores.txt")

the_plot <- ggplot(d,
       aes(x=word,y=score)) + 
        geom_line() + 
        theme_minimal() +
        scale_x_continuous(label=comma) + 
        facet_wrap(~president, scales = "free") +
        labs(caption=expression(paste(italic("Graphique de Tony Layton")))) +
        labs(x="Word Position in Inaugurations",
        y="Running Sentiment Score",
        title="Sentiment of Each Presidents Inaugural Speech\nOver the Course of the Speech") + 
        stat_smooth(se=F)

ggsave("Presidential_Inauguration_Sentiment.jpg", plot = the_plot, device = "jpg", path = NULL,
       scale = 1, width = 18, height = 12, units = "in",
       dpi = 600, limitsize = FALSE)
