#import packages and load the data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
facebook_network=pd.read_csv("https://snap.stanford.edu/data/facebook_combined.txt.gz",header=None,sep=" ")
names=pd.read_csv("https://people.cam.cornell.edu/md825/names.txt",header=None,sep=",")

#turn the two dataset into dataframes
facebook_network_df=pd.DataFrame(facebook_network)
names_df=pd.DataFrame(names)

#Initializing a new dataframe as draft
df_draft=pd.DataFrame()
df_draft["Name"]=names_df[1]

# Group by the first column and the second column individually
# Add them together to get number of friends for each person
df_draft["num_of_friends_pt1"]=facebook_network_df.groupby(0).size()
df_draft.num_of_friends_pt1=df_draft.num_of_friends_pt1.fillna(0)
df_draft["num_of_friends_pt2"]=facebook_network_df.groupby(1).size()
df_draft.num_of_friends_pt2=df_draft.num_of_friends_pt2.fillna(0)
df_draft["NbrFriends"]=df_draft.num_of_friends_pt1+df_draft.num_of_friends_pt2
df_draft.head(10)

#Getting our intended df dataframe from the draft
df=df_draft[['Name', 'NbrFriends']] 
df.head(10)

#Checking the shape of our dataframe (4039,2)
print(df.shape)

#Find the max/min num of friends value
max_value = df["NbrFriends"].max()
min_value = df["NbrFriends"].min()
#print(max_value)
#print(min_value)

#Find all rows that satisfy the max/min criterion
most_social=df[df['NbrFriends']==max_value]
least_social=df[df['NbrFriends']==min_value]


#Printing out the rows
for i,v in most_social.iterrows():
    print("{} is a very sociable person, he has {} friends.".format(v[0],str(int(v[1]))))
for i,v in least_social.iterrows():
    print("{} is a solitary person, he has only {} friends.".format(v[0],str(int(v[1]))))


#Outputing the mean/median/variance to output2.txt file
writer=open("output2.txt","w+")
average=np.mean(df['NbrFriends'])
median=np.median(df['NbrFriends'])
variance=np.var(df['NbrFriends'])
writer.write("Average:{},\nMedian: {},\nVariance: {}".format(average,median,variance))
writer.close()

#Output the plot as pdf
plot=plt.figure()
plt.hist(df['NbrFriends'])
plt.show()
plot.savefig("output2.pdf")


