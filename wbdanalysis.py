'''
World Bank Data - Analyzing and Plotting
'''

#Importing Pandas and Matplotlib
import pandas as pd
import matplotlib.pyplot as plt 


def plot_pop(filename, country_code):

	#To get the Country Name for displaying it in Plot in the Title Field
	#-------------------------------------------------------------------

	#Reading CSV as a whole
	wbd = pd.read_csv(fn)

	#Getting List of Indexes where that Country Code is present in the DataSet
	list_index_country = wbd.index.values[wbd['CountryCode']== country_code]
	index_country = list_index_country[0]

	#Getting the Name and Index of the country and converting them to a dictionary
	location = wbd.iloc[[index_country],[0]]
	location_dict = dict(location)

	#Using key Values in Dictionary Extracting the Country Name and storing it into cname
	[(k,v)] = location_dict.items()
	cname = v.values[0]
	#-------------------------------------------------------------------

	#Reading Large data in Chunks of 1000 pieces
	urb_pop_reader = pd.read_csv(filename, chunksize=1000)

	#Creating an empty DataFrame
	data= pd.DataFrame()

	for df_urb_pop in urb_pop_reader:

		#Extracting Country Data which was passed in function "plot_pop()"
		df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == country_code]

		#Zipping the Total and The Urban Population of that specified country in country_code
		pops = zip(df_pop_ceb['Total Population'], df_pop_ceb['Urban population (% of total)'])

		#Creating List frok the Zip
		pops_list = list(pops)

		#Adding Total Urban Population in the DataFrame along with Total and Urban(% of Total)
		df_pop_ceb['Total Urban Population'] = [int(tup[0] * tup[1]* 0.01) for tup in pops_list]
		data = data.append(df_pop_ceb)

	#Plotting the Graph for the Population Change over the span of 50 years
	data.plot(kind='scatter', x='Year', y='Total Urban Population', title= cname)

	plt.show()

fn = 'world_ind_pop_data.csv'

#Showing Plots of BRICS Countries Data of 50 years
plot_pop(fn, 'BRA')
plot_pop(fn, 'RUS')
plot_pop(fn, 'IND')
plot_pop(fn, 'CHN')
plot_pop(fn, 'ZAF')