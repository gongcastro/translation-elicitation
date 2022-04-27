

# stimuli_transformed <- stimuli %>% 
#     mutate(
#         word = word %>% 
#             gsub("á", "a", .) %>% 
#             gsub("r", "0", .)
#     ) 

library(dplyr)

data.frame(
    word = c("árbol", "cómo")
) %>% 
    mutate(
        word_replaced = gsub("á", "a", word) 
    ) %>% 
    print()

# process responses


