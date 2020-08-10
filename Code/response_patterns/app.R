#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)
library(dplyr)
library(scales)
library(stringr)
library(ggplot2)

integer_breaks <- function(n = 5, ...) {
    fxn <- function(x) {
        breaks <- floor(pretty(x, n, ...))
        names(breaks) <- attr(breaks, "labels")
        breaks
    }
    return(fxn)
}

dat <- fread(here("Data", "03_accuracy_coded.csv"), na.strings = c("", "NA")) %>% 
    as_tibble() %>% 
    mutate_at(vars(same_onset, group), as.factor) %>% 
    mutate(valid_response = response_type %in% c("correct", "typo", "wrong", "false_friend"),
           correct_coded = response_type %in% c("correct", "typo"),
           correct_coded = ifelse(correct_coded, "Correct", "Wrong"),
           group = as.factor(group),) %>%
    filter(valid_response) %>% 
    group_by(trial_id, word, response_type, group, input_text) %>%
    summarise(n = n(), .groups = "drop") %>% 
    arrange(trial_id, -n) %>% 
    mutate(input_text = fct_inorder(input_text)) %>% 
    group_by(trial_id) %>% 
    slice_head(n = 5) %>% 
    ungroup() %>% 
    mutate(response_type = str_to_sentence(response_type))


# Define UI for application that draws a histogram
ui <- fluidPage(
    
    # Application title
    titlePanel("Old Faithful Geyser Data"),
    
    # Sidebar with a slider input for number of bins 
    sidebarLayout(
        sidebarPanel(
            selectInput(inputId = "group",
                        label = "Group: ",
                        choices = unique(dat$group),
                        selected = unique(dat$group),
                        multiple = TRUE),
            selectInput(inputId = "word",
                        label = "Word: ",
                        choices = unique(dat$word))),
        # Show a plot of the generated distribution
        mainPanel(
            plotOutput("responsesPlot")
        )
    )
)

# Define server logic required to draw a histogram
server <- function(input, output) {
    
    output$responsesPlot <- renderPlot({

        target_trials <- dat %>%
            group_by(trial_id) %>% 
            slice_max(order_by = n, n = 5) %>% 
            group_by(trial_id) %>% 
            summarise(n = min(n), .groups = "drop")
        
        # draw the histogram with the specified number of bins
        #### visualise data ######################
        dat %>%
            filter(word %in% input$word,
                   group %in% input$group,
                   trial_id %in% target_trials$trial_id) %>% 
            ggplot(aes(x = input_text, y = n, fill = response_type)) +
            facet_wrap(~group, scales = "free_x") +
            geom_col() +
            labs(x = "Typed response", y = "Counts", fill = "Coded as...") +
            scale_color_brewer(palette = "Set1") +
            scale_y_continuous(breaks = integer_breaks()) +
            theme_classic() +
            theme(legend.position = "top",
                  panel.border = element_rect(colour = "black", fill = NA),
                  panel.grid.major.y = element_line(colour = "grey", linetype = "dotted"),
                  axis.text = element_text(colour = "black"),
                  text = element_text(size = 20))
    })
}

# Run the application 
shinyApp(ui = ui, server = server)
