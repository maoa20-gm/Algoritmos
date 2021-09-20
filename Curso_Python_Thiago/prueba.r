library(tidyverse)
library(janitor)
library(lubridate)

birth <- read.csv("/home/maoa/Documents/Algoritmos/Curso_Python_Thiago/PE_TODOS2.csv")


birth %>% clean_names() -> birth # Eu coloquei os nomes em minuscula, nao gosto as maisculas

cols.fact <- c("ano_nasc", "estcivmae" , "escmae","racacor")

birth[cols.fact] <- sapply(birth[cols.fact], as.character)

birth %>% 
  mutate_if(is.character, as.factor) %>% 
  mutate(data_nasc = mdy(data_nasc))-> birth

cantidad <- birth %>%                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
    group_by(data_nasc,ano_nasc) %>% 
    count(data_nasc,sort = F) 
                                                                            

ggplot(cantidad, aes(x = ano_nasc, y = n, color = ano_nasc)) +
  geom_boxplot() +
  geom_jitter() +
  scale_color_brewer(type = "qual", palette = 2) +
  theme_minimal() +
  theme(legend.position = "none")+
    labs( x = "",
       y = "Numero de nascidos vivos")

birth %>%
  mutate(classe = as.character(classe)) %>% 
  mutate(classe = as.factor(classe)) -> birth

  escolaridade <- birth %>% 
  group_by(escmae) %>% 
  summarise(n= n()) %>% 
  arrange(desc(n))

estado <- birth %>% 
  group_by(estcivmae) %>% 
  summarise(n= n())

raca <- birth %>% 
  group_by(racacor) %>% 
  summarise(n= n())


p1<-ggplot(data = escolaridade) + 
  geom_col(mapping = aes(x = escmae, y = n, fill = escmae), show.legend = F)+
  scale_y_continuous(labels = scales::comma)+
  scale_x_discrete(limits = c("1","2", "3", "4", "5"),
                   labels = c("Nenhuma", "1 a 3 anos", "4 a 7 anos", "8 a 11 anos", "12 e mais"))+
  theme_classic()+
  labs(x = "Escolaridade", y = "número de maes")+
  scale_fill_manual(values = c("#8dd3c7", "#ffffb3", "#bebada", "#fb8072", "#80b1d3"))

p1
