import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df= pd.read_csv('fcc-forum-pageviews.csv',index_col='date',parse_dates=['date'])

# Clean data
df=df[(df['value']>=df['value'].quantile(0.025))&(df['value']<=df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot

    fig,ax=plt.subplots(figsize=(20,9))
    sns.lineplot(df,y='value',x='date',color='r',linewidth=2.5)
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    sns.lineplot(data=df, legend=False)
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = None
    df_bar=df.copy()
    dict = {
        'value':[0,0,0,0],
        'date':['2016-01-01', '2016-02-01', '2016-03-01', '2016-04-01']
       }
    df_bar.loc['2016-01-01 00:00:00'] = [0]
    df_bar.loc['2016-02-01 00:00:00'] = [0]
    df_bar.loc['2016-03-01 00:00:00'] = [0]
    df_bar.loc['2016-04-01 00:00:00'] = [0]
    df_bar.index = pd.to_datetime(df_bar.index)
    # df_bar = df_bar._append(dict, ignore_index = True)
    df_bar['day']=df_bar.index.day
    df_bar['month']=df_bar.index.month
    df_bar=df_bar.sort_values(['month'])
    # print(df_bar)
    df_bar.month=df_bar.month.map({1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"})
    df_bar['year']=df_bar.index.year
    # Draw bar plot
    
    fig,ax=plt.subplots(figsize=(20,10))

    pal=sns.color_palette('bright',12)

    sns.barplot(df_bar,x='year',y='value',hue='month',palette=pal,errorbar=None)
    # sns.move_legend(fig, "upper left",  title="Months",bbox_to_anchor=(0, 1)).fig

    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    df_box['monthnum']= [d.month for d in df_box.date]
    df_box=df_box.sort_values(['monthnum'])
    # Draw box plots (using Seaborn)
    
    fig,(ax1,ax2)=s=plt.subplots(ncols=2,figsize=(28,8))
    sns.boxplot(ax=ax1,data=df_box,
        flierprops={"marker": "."},dodge=False,
        hue='year',width=0.8,    whis=1.5,
        x='year',y='value').set_title("Year-wise Box Plot (Trend)")
    ax1.set_xlabel('Year')
    ax1.legend([], [], frameon=False)
    ax1.set_ylabel('Page Views')
    sns.boxplot(ax=ax2,data=df_box,
        dodge=False,flierprops={"marker":'.'},
        hue='month',width=0.8,    whis=1.5,
        x='month',y='value')
    ax2.set_title("Month-wise Box Plot (Seasonality)")
    ax2.set_xlabel('Month')
    
    ax2.set_ylabel('Page Views')
    ax2.legend([], [], frameon=False)    



    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
