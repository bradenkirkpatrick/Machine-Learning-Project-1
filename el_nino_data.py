years = range(1951, 2025)
jan_values = [
    2.5, -1.5, 0.5, 1.1, -0.9, 2.2, 1.0, -3.1, -1.5, 
    0.2, -0.4, 3.3, 1.7, -0.6, -0.7, -2.2, 2.8, 0.9, 
    -2.4, -1.9, 0.6, 0.8, -0.5, 4.0, -0.8, 2.3, -0.7, 
    -0.5, -0.7, 0.7, 0.6, 2.0, -5.8, 0.3, -0.5, 1.6, 
    -1.1, -0.2, 2.5, -0.1, 1.0, -4.7, -1.5, -0.2, -0.7, 
    1.6, 0.8, -4.4, 3.0, 1.1, 1.6, 0.7, -0.3, -2.2, 
    0.6, 2.7, -1.3, 2.9, 1.8, -1.8, 3.8, 1.8, -0.1, 
    2.4, -1.4, -3.6, 0.3, 1.8, -0.1, .3, 3.2, 0.8, 2.3, 
    0.8
]
feb_values = [  
    1.5, -1.0, -0.8, -0.5,
    3.1, 2.7, -0.1, -0.8, -2.3, 0.2, 1.5, -0.5, 0.9, 0.7, 
    -0.4, 2.8, 2.1, -0.9, -1.7, 3.3, 1.8, -2.3, 3.4, 1.3,
    2.8, 2.0, -4.4, 1.6, 0.5, -0.3, 0.4, -6.0, 1.4, 2.0,
    -1.7, -1.1, -2.1, -0.6, 2.0, -3.0, 0.4, -1.5, -1.2, 0.4,
    -0.2, 0.4, 2.9, -3.4, 1.6, 2.7, 2.8, 1.8,-1.1, 2.0,
    -5.2, 0.2,  -0.1, 4.4, 3.1, -2.4, 4.5, 0.8, -0.4, 0.1,
    0.4, -3.2, -0.1, -0.8, -2.3, -0.1, 2.5, 1.8, 2.3, -2.3
]
import pandas
df = pandas.DataFrame(data={"year": years, "jan_nino": jan_values, "feb_nino": feb_values})
df.to_csv("./el_nino_data.csv", sep=",",index=False)