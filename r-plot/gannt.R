library("xlsx")
library("ganttrify")
library("viridis")

# Variables
font <- "Arial"
start_date <- "2023-01"
excelfilename <- "gannt.xlsx" # Workbooks "Gannt" and "Milestones" are required

f <- viridis(8)

setwd(dirname(rstudioapi::getActiveDocumentContext()$path))
getwd()
activities <- read.xlsx(excelfilename, sheetName="Gannt")
milestones <- read.xlsx(excelfilename, sheetName="Milestones")

# Remove NAs when Excel acts weird
activities <- na.omit(activities)
milestones <- na.omit(milestones)
#activities <- activities[ , colSums(is.na(activities)) == 0]
#milestones <- milestones[ , colSums(is.na(milestones)) == 0]
View(activities)
# Customizing the output
pdf("gannt.pdf",            
    width = 400, height = 50,  
    bg = "white",          
    colormodel = "cmyk",   
    paper = "A4r")           

# Creating a plot
ganttrify(project =activities,
          project_start_date = start_date,
          size_text_relative = 0.9, 
          mark_quarters = TRUE,
          spots = milestones,
          colour_palette = f,
          font_family = font)


    # Closing the graphical device
dev.off() 


png("gannt.png",            
    width = 2600, height = 1000,  
    bg = "white")           

# Creating a plot
ganttrify(project =activities,
          project_start_date = start_date,
          size_text_relative = 1.4, 
          mark_quarters = TRUE,
          spots = milestones,
          colour_palette = f,
          font_family = font)


# Closing the graphical device
dev.off() 

