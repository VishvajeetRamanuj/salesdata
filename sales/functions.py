'''
Ownership : 
Vnurture Technologies

Developed for Training Purpose
Unauthoied copy and distribution is proibited 

Contact for usage/distribution : 
shahnikhilb@gmail.com

info@vnurture.in

Matplotlib: Python based plotting library offers matplotlib
 with a complete 2D support along with limited
 3D graphic support. 
 It is useful in producing publication quality 
 figures in interactive environment across platforms.
 It can also be used for animations as well.
 To know more about this library, check this link.
 https://matplotlib.org/

Seaborn: Seaborn is a library for creating informative 
and attractive statistical graphics in python. 
This library is based on matplotlib. 
Seaborn offers various features such as built in themes,
 color palettes, functions and tools to visualize univariate,
 bivariate, linear regression, matrices of data,
 statistical time series etc which lets us to build 
 complex visualizations.
 http://seaborn.pydata.org/
 
 
 RAW DATA
41_Expmoyee_sales_data_gender.xlsx 
======================== 
 s	GENDER	AGE	Sales	BMI	Income EnglishSpeaking
E1	M	34	123	Normal	350
E2	F	40	114	Overweight	450
E3	F	37	135	Obesity	169
E4	M	30	139	Underweight	189
E5	F	44	117	Underweight	183
E6	M	36	121	Normal	80
E7	M	32	133	Obesity	166
E8	F	26	140	Normal	120
E9	M	32	133	Normal	75
E10	M	36	133	Underwight	40


PLOT Various Graphs

 
'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# this function will take csvfile and create figure and save it from where django will show image to 
# website
def create_plot_from_xlsx(filename, sheet_name):
    df=pd.read_excel(filename, sheet_name)


    #######################
    #Histogram : Age wise and Income wise
    ########################

    fig=plt.figure() #Plots in matplotlib reside within a figure object, use plt.figure to create new figure
    #Create one or more subplots using add_subplot, because you can't create blank figure
    ax = fig.add_subplot(1,1,1)
    #Variable
    ax.hist(df['Age'],bins = 3) # Here you can play with number of bins labels and Tit
    plt.title('Age distribution')
    plt.xlabel('Age')
    plt.ylabel('#Employee')
    # plt.show()

    # saving figure
    fig.savefig('sales/static/sales/age_histogram.png', dpi=300)


    fig1=plt.figure()
    ax1 = fig1.add_subplot(1,1,1)
    #Variable
    ax1.hist(df['Income'],bins = 5) # Here you can play with number of bins Labels and Tit
    plt.title('Income distribution')
    plt.xlabel('Income')
    plt.ylabel('#Employee')
    # plt.show()

    # saving figure
    fig1.savefig('sales/static/sales/income_distribution.png')

    ##############
    #BOXPLOT# AGE WISE 
    # 44 age is outliar
    #################

    fig=plt.figure()
    ax = fig.add_subplot(1,1,1)
    #Variable
    ax.boxplot(df['Age'])
    # plt.show()

    fig.savefig('sales/static/sales/age_box_plot.png')


    ###################
    #Violin Plot  age on y  vs gender on x
    #usingf seaborn  for 3D impact
    '''A violin plot is a method of plotting numeric data.
    It is similar to box plot with a rotated kernel density
    plot on each side. A violin plot has four layers.


    A Violin Plot is used to visualise the distribution
    of the data and its probability density.

    This chart is a combination of a Box Plot and a 
    Density Plot that is rotated and placed on each side, 
    to show the distribution shape of the data. 
    The thick black bar in the centre represents the 
    interquartile range, the thin black line extended from 
    it represents the 95% confidence intervals, 
    and the white dot is the median.

    Box Plots are limited in their display of the data,
    as their visual simplicity tends to hide significant
    details about how values in the data are distributed. 
    For example, with Box Plots, you can't see if the 
    distribution is bimodal or multimodal. While Violin 
    Plots display more information, they can be 
    noisier than a Box Plot.


    seaborn.despine(fig=None, ax=None, top=True, right=True, left=False, bottom=False, offset=None, trim=False)
    Remove the top and right spines from plot(s).
    '''
    #######################

     
    sns.violinplot( df['Gender'],df['Age']) #Variable Plot
    #sns.despine()


    ######################
    #BARCHART
    #
    #PLOT sales by males/Females 
    ##################

    var = df.groupby('Gender').Sales.sum() #grouped sum of sales at Gender level
    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)
    ax1.set_xlabel('Gender')
    ax1.set_ylabel('Sum of Sales')
    ax1.set_title("Gender wise Sum of Sales")
    var.plot(kind='bar')
    fig.savefig('sales/static/sales/gender_bar_plot.png', dpi=300)

    ######################
    #BARCHART
    #
    #PLOT sales by BMI level
    ##################

    var = df.groupby('BMI').Sales.sum() #grouped sum of sales at Gender level
    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)
    ax1.set_xlabel('BMI')
    ax1.set_ylabel('Sum of Sales')
    ax1.set_title("BMI wise Sum of Sales")
    var.plot(kind='bar')
    fig.savefig('sales/static/sales/bmi_bar_plot.png', dpi=300)

# calling function for actual process
# create_plot_from_xlsx("41_Expmoyee_sales_data_gender.xlsx", "Sheet1")
                    #    41_Expmoyee_sales_data_gender.xlsx

###############################
# HEATMAP - AIrpasenger data from R Studio
#monthly totals for airline passengers from 1949 to 1960 
#on a specific route.  
# using seaborn
################################
##      Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
## 1949 112 118 132 129 121 135 148 148 136 119 104 118
## 1950 115 126 141 135 125 149 170 170 158 133 114 140
## 1951 145 150 178 163 172 178 199 199 184 162 146 166
## 1952 171 180 193 181 183 218 230 242 209 191 172 194
## 1953 196 196 236 235 229 243 264 272 237 211 180 201
## 1954 204 188 235 227 234 264 302 293 259 229 203 229
## 1955 242 233 267 269 270 315 364 347 312 274 237 278
## 1956 284 277 317 313 318 374 413 405 355 306 271 306
## 1957 315 301 356 348 355 422 465 467 404 347 305 336
## 1958 340 318 362 348 363 435 491 505 404 359 310 337
## 1959 360 342 406 396 420 472 548 559 463 407 362 405
## 1960 417 391 419 461 472 535 622 606 508 461 390 432
#

'''
import seaborn as sns


flights_raw = pd.read_csv('41_Airflights_data_selfmade.csv')
flights_raw["month"] = pd.Categorical(flights_raw["month"], flights_raw.month.unique())
print(flights_raw.head())

flight_matrix = flights_raw.pivot("month", "year", "passengers")

fig = plt.figure(figsize=(12,12))
r = sns.heatmap(flight_matrix, cmap='BuPu')
r.set_title("Heatmap of Flight Density from 1949 to 1960")


Contact for usage/distribution /Training : 
shahnikhilb@gmail.com
info@vnurture.in
'''
