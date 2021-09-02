import streamlit as st 
import warnings
warnings.filterwarnings('ignore')
st.set_option('deprecation.showPyplotGlobalUse', False)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt  
import seaborn as sns
from scipy import stats
from PIL import Image
import webbrowser
import streamlit.components.v1 as components

st.markdown('''
**Data Visualization App**
This app helps you to get the **Graphs and Plots** of your data
**App built in 'Streamlit' using Python**
''')

#https://giphy.com/explore/plots
st.image("https://media.giphy.com/media/l46Cy1rHbQ92uuLXa/giphy.gif", width= 500)




user_file= st.sidebar.file_uploader("Upload your CSV file")

dataset= 'heart.csv'

if user_file is not None:
	
	def csv():
		df= pd.read_csv(user_file)
		return df
	data= csv()

	st.header('**Your Data**')
	st.write(data)


	new_data = data.select_dtypes(include='number')
    
        
	l= list(new_data.columns)
	for i in range(len(l)):
				vals= new_data[l[i]].values[0]
				#st.write(vals)
				n= len(str(vals))
				if n>=7:
						new_data= new_data.drop([l[i]], axis = 1)
				else:
						new_data = new_data

	modified = new_data
	components.html("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """)
	st.image("https://i.gifer.com/7l6J.gif", width= 400)
	if st.button("Click here to see Line Chart"):
		new1= pd.DataFrame(modified) 
		#st.write(modified)  
		l = list(new1.columns)
	
		cols1= []
		cols2= []
		for i in range(len(l)):
				sets = set(new1[l[i]].values)
				total= len(sets)
				#st.write(total)
				if total>= 7:
						col= l[i]
						cols1.append(col)
				elif total<7:
						cols2.append(l[i])
		l= list(new1.columns)
		c= ['Year','YEAR','year','Time','TIME', 'time','Hour','HOUR','hour','Day','DAY','day']
		count=0
		#st.write(cols1)
		#st.write(cols2)
		for k in cols2:
				new1= new1.drop(k, axis= 1)
				#st.write(new1)
		for i in l:
				if i in c:
					count+=1
					if count>=1:
						r= new1.sort_values(by= i)
						#st.write(r)
						j= r.drop([i],axis= 1)
						#st.write(j)
						l1= list(j.columns)
						for k in l1:
						
							plt.figure(figsize=(12,6))
							plt.plot(new1[i][:100],new1[k][:100],color = 'red')
							plt.xlabel(i, fontsize= 13)
							plt.ylabel(k, fontsize= 13)
							st.pyplot()
				elif count==0:
			            
					st.line_chart(new1)
					break
	
	components.html("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """)
	st.image("https://media.giphy.com/media/r7Rwd7KDGhzoiJt6vZ/giphy.gif?cid=ecf05e47j3dh7itxfksh44erjg4abldm1f9hx5tcrw4u2yfc&rid=giphy.gif&ct=g", width= 400)
	if st.button("Click here to see Bar Chart"): 
		dfs= pd.DataFrame(modified)
		l = list(dfs.columns)
		cols_1= []
		cols_2=[]
		for i in range(len(l)):
			sets = set(dfs[l[i]].values)
			total= len(sets)
			if total>=2 and total<=10:
				col= l[i]
				cols_1.append(col)
			else:
				cols_2.append(l[i])
		if len(cols_1)==0 or len(cols_2)==0:
			st.bar_chart(modified)
		else:
			for i in cols_1:
				for j in cols_2:
					sns.barplot(x= i, y= j,data= data, hue= i,palette= 'magma')
					plt.xlabel(i)
					plt.ylabel(j)
					st.pyplot()
            
	components.html("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """)
	st.image("https://assets.holoviews.org/gifs/guides/user_guide/Streaming_Data/streamz7.gif", width= 400)
	if st.button("Click here to see Histogram Plots"):
		k= new_data.columns
		l= list(k)
		for i in range(len(l)):
			h= []
			n= new_data[l[i]].values
			h.append(n)
			plt.figure(figsize=(3,2))
			plt.hist(h)
			plt.xlabel(l[i], fontsize= 10)
			plt.ylabel("Frequency", fontsize= 10)
			st.pyplot()
            
	components.html("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """)      
	st.image("https://www.r-graph-gallery.com/img/graph/3-r-animated-cube.gif",width=500)
	if st.button("Click here to see Scatter Plots"):  
		dfs= pd.DataFrame(modified)
		l = list(dfs.columns)
		cols_3= []
		cols_4=[]
		cols_2= []
		for i in range(len(l)):
			sets = set(dfs[l[i]].values)
			total= len(sets)
			if total==2:
				col= l[i]
				cols_3.append(col)
			elif total> 10:
				cols_2.append(l[i])
			else:
				cols_4.append(l[i])
		#st.write(cols_3)
		for i in cols_2:
			a= modified
			x1= a.drop([i],axis=1)
			#st.write(x1)
			for j in x1:
					sns.scatterplot(x=modified[i],y=modified[j])
					st.pyplot()
             
		
	components.html("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """)      
	st.image("https://www.disruptive-technologies.com/hubfs/Google%20Drive%20Integration/Why%20Heatmaps%20Are%20A%20Powerful%20Tool%20for%20Facilities%20Management-3.gif",width=500)        
	if st.button("Click here to see Heatmap"):
		a= new_data.corr()
		annot = True
		linecolor = "yellow"
		linewidths= 1
		plt.figure(figsize=(10,8))
		plt.title("Correlation of Features")
		sns.heatmap(a,annot= annot,linewidths=linewidths,linecolor=linecolor)
		st.pyplot()
    
	st.markdown('''**-------------------------------------------------------------------------------------------------------**''')










else:
	st.info('Please upload your CSV file to see plots for your data')
	if st.button('See the Plots of a Sample Dataset'):
		data= pd.read_csv(dataset)
		st.write(data)

		

		new_data= data.select_dtypes(include= 'number')

		components.html("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """)      
		st.header("Line Chart")
		new= pd.DataFrame(new_data)
		st.line_chart(new)
        
		components.html("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """)      
		st.header("Bar Chart")
		st.bar_chart(new_data)

		components.html("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """)      
		st.header("Histogram Plots")
		k= new_data.columns
		l= list(k)
		j= 1
		for i in range(len(l)):
				h= []
				n= new_data[l[i]].values
				h.append(n)
				plt.figure(figsize=(3,2))
				plt.hist(h)
				plt.legend()
				plt.xlabel(l[i], fontsize= 10)
				plt.ylabel("Frequency", fontsize= 10)
				st.pyplot()

		components.html("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """)      
		st.header("Scatter Plots") 
		dfs= pd.DataFrame(new_data)
		l = list(dfs.columns)
		cols_3= []
		cols_4=[]
		cols_2= []
		for i in range(len(l)):
			sets = set(dfs[l[i]].values)
			total= len(sets)
			if total==2:
				col= l[i]
				cols_3.append(col)
			elif total> 10:
					cols_2.append(l[i])
			else:
					cols_4.append(l[i])
		#st.write(cols_3)
		for i in cols_2:
			a= new_data
			x1= a.drop([i],axis=1)
			#st.write(x1)
			for j in x1:
					sns.scatterplot(x=new_data[i],y=new_data[j])
					st.pyplot()
             
		components.html("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """)      
		st.header("Heatmap")
		a= new_data.corr()
		annot = True
		linecolor = "yellow"
		linewidths= 1
		plt.figure(figsize=(10,8))
		plt.title("Correlation of Features")
		sns.heatmap(a,annot= annot,linewidths=linewidths,linecolor=linecolor)
		st.pyplot()
		st.markdown('''**-----------------------------------------------------------------------------------------------------------**''')
