import seaborn as sns
import matplotlib.pyplot as plt
#df = dataframe conating x and y labels
#cols = feature columns 

def kde_target(var_name, df):
    
    # Calculate the correlation coefficient between the new variable and the target
    corr = df['Churn'].corr(df[var_name])
    
    # Calculate medians for one target variable  vs other target variable
    target_y1 = df.ix[df['Target'] == 0, var_name].median()
    target_y2 = df.ix[df['Target'] == 1, var_name].median()
    
    plt.figure(figsize = (12, 6))
    
    # Plot the distribution for target == 0 and target == 1
    sns.kdeplot(df.ix[df['Target'] == 0, var_name], label = 'Target == 0')
    sns.kdeplot(df.ix[df['Target'] == 1, var_name], label = 'Target == 1')
    
    # label the plot
    plt.xlabel(var_name); plt.ylabel('Density'); plt.title('%s Distribution' % var_name)
    plt.legend();
    plt.savefig('Kde_plot_1/'+var_name+'.png')
    # print out the correlation
    print('The correlation between %s and the TARGET is %0.4f' % (var_name, corr))
    # Print out average values
    print('Median value for loan that was not repaid = %0.4f' % target_y2)
    print('Median value for loan that was repaid =     %0.4f' % target_y1)
    
for col in df.columns:
    kde_target(col,df)