---
title: "England Blanket Bog Model ReadMe"
author: "CK"
date: "6 October 2017"
output: html_document
---

## About
We are developing a model which can predict the presence of blanket bog where it is found in England.    

## Progress
A number of random forest models have been fitted for Cumbria, and one model has been chosen to predict blanket bog in Cumbria. 

###Model details: 

####Main branch

This is initially based on Cumbria

M.rf.3.final
Random Forest 

1106 samples
  15 predictor
   2 classes: 'absent', 'present' 

No pre-processing
Resampling: Bootstrapped (25 reps) 
Summary of sample sizes: 1106, 1106, 1106, 1106, 1106, 1106, ... 
Resampling results across tuning parameters:

  mtry  Accuracy   Kappa    
   2    0.9349493  0.8686078
   8    0.9341944  0.8671090
  15    0.9301934  0.8589484

Accuracy was used to select the optimal model using the largest value.
The final value used for the model was mtry = 2.

Coefficients:
"elev"          "aspect"        "slope"         "outflow"       "inflow"       
"surf"          "gdd"           "gsl"           "rain_ann"      "rain_daily"   
"raindays_10mm" "raindays_1mm"  "temp_mean"     "temp_min"      "temp_max"   

See notebook/bb_run_models.3.nb.html for more info. 

**need to update this up to model 7a**

####Yorkshire Dales Pilot branch

Following Model 7a, trying the approach out on a different area: Yorkshire Dales and Nidderdale.  Main lessons from Model 7a: 

* general approach OK
* output should be probability of blanket bog potential   
*	moorland line operates very differently in some areas (e.g. it’s actually in the valleys in the Derbyshire Dales) and it reflects land management intervention, which we are (sort of by definition) trying to see beyond.  So needs a rethink.  
*	How does it relate to the National Soils Map (the Cranfield one)  
* age of the climate data I’ve been using (period 1960 to 1990): still makes sense to train the model on the historic data, because its more closely reflects the conditions the bog developed.  However for predicting potential we can use most recent climate data (early 2000s), and climate projections, see below. *	develop scenarios for blanket bog potential under different climate projections  



## Source Data

### Predictors
The predictors used in this model are as follows: 

#### CLIMATE DATA
All climate data was derived from *UKCP09: Met Office gridded land surface climate observations - long term averages at 5km resolution* (Met Office, 2017).  We have used the 1960 to 1990 long term averages (averages for more recent time periods are also available) on the assumption that blanket bog presence is most likely to correlate with historic climate than recent climatic changes.  However this needs to be tested against other ranges of available climate data and it other variables which determine extent of blanket bog.   

Full methodology and lots of further information is available from Met Office 2017, and in Perry et al, 2005.  The monthly long-term averages were aggregated to seasonal and annual data using the same methodology as the Met Office used for its 25km seasonal averages:  

>For the days of frost and days of rain variables the seasonal and annual averages are the total of the individual monthly averages. For the remaining variables the seasonal and annual averages are the mean of the monthly averages (allowing for differences in month length). To facilitate combining the baseline data with the UKCP09 climate projections, the 25 km baseline averages for rainfall have been expressed in units of millimetres per day (rather than total millimetres, as for the 5 km data sets).

Each season is comprised of three calendar months, as follows:  

* Winter = December, January, February  
* Spring = March, April, May  
* Summer = June, July, August  
* Autumn = September, October, November  

The following datasets are used as predictors in the model:  

|Dataset|Units|
|:----|:----|
|Growing degree days annual average|days|
|Growing season length annual average|days|
|Total rainfall annual average|mm|
|Mean daily rainfall annual average|mm|
|Days of rain above 10mm annual average|days|
|Days of rain above 1mm annual average|days|
|Mean annual maximum temperature|deg C|
|Mean annual temperature|deg C|
|Mean annual minimum temperature|deg C|

#### Topographic and hydrological data

TBC

### Training data
The model will be trained on `EXPLAIN TRAINING DATA` 

## Models
*explain what models are used, what models were tried and rationale for choice.* 

## Project information
This project was carried out in `R` (R Core Team, 2016) and is a mixture of `R script` (`.R`) and `Rmarkdown  Notebook` (`.rmd`).  The code in this repository is intended to be run in the order below.  However any data output from one script that is to be passed forward to a later script has been saved with `save()` either as  `.rda` file or as a raster stack into a `.tiff` file.  The later script then loads the files.  This is particularly useful for the `.Rmd` files which can all be independently 'knitted'.  Currently, no scripts are 'sourced' into another script.  

|Script filename|Type|Purpose|
|:--------------|:---|:---------------------------------------------|
|ukcp09DataImport.R|R script|imports climate data as `ESRI ASCII` files, converts to raster and calculates seasonal and annual averages|
|bb_data_prep.Rmd|Rmarkdown|data preparation. Imports topo and hydro `.tiff` files and converts to raster, calculates slope and aspect rasters, resamples climate rasters|
|bb_input_data.Rmd|Rmarkdown|Creates input dataset for models by extracting location info from peat depth file and extracting predictor variables from rasters|
|bb_model_selection.Rmd|Rmarkdown|Runs a number of models and assesses performance|
|bb_model_run.Rmd|Rmarkdown|Runs final model and creates final outputs|
|bb_predict.Rmd|Rmarkdown|Uses model to predict blanket bog with a raster stack of predictors|


## References

Met Office (2017): UKCP09: Met Office gridded land surface climate observations - long term averages at 5km resolution. Centre for Environmental Data Analysis, accessed on 01/10/2017. http://catalogue.ceda.ac.uk/uuid/620f6ed379d543098be1126769111007

Perry, Matthew, and Daniel Hollis. "The generation of monthly gridded datasets for a range of climatic variables over the United Kingdom." International Journal of Climatology 25.8 (2005): 1041-1054. https://www.metoffice.gov.uk/binaries/content/assets/mohippo/pdf/p/8/monthly_gridded_datasets_uk.pdf

R Core Team (2016). "R: A language and environment for statistical computing. R Foundation for Statistical Computing"", Vienna, Austria. URL http://www.R-project.org/.
