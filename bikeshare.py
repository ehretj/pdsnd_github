import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). 
    while True:
        city=input("\nWould you like to see data for Chicago, New York, or Washington?\n")
        city=city.lower()
        if city in ('chicago','new york','washington'):
            print('\nYou Chose {}.'.format(str.capitalize(city)))
            break
        else:
            print('\nPlease Choose from the list of Cities !\n')
     # get user input for month (all, january, february, ... , june)
    while True:
        month=input("\nWhich month from January to June?\n")
        month=month.lower()
        if month in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            print('\nYou Chose {}.'.format(str.capitalize(month)))
            break
        else:
            print('\nChoose from January, February, March, April, May, June or all?')
      # get user input for day of week (all, monday, tuesday, ... sunday)      
    while True:
        day=input("\nWhich day of the week?\n")
        day=day.lower()
        if day in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'):
            print("\nYou Chose {}.".format(str.capitalize(day)))
            break
        else:
            print('\nChoose from Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all')
           
    print('-'*40)
    return city, month, day 

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df=pd.read_csv(CITY_DATA[city])
    # Convert Start Time to date Time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # Exctract Month Data from Start Time Column
    df['month'] = df['Start Time'].dt.month
    # Exctract Days Data from Start Time Column
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # Exctract hours Data from Start Time Column
    df['hour'] = df['Start Time'].dt.hour
    
    # filter by month if applicable
    if month != 'all':
    # use the index of the months list to get the corresponding int   
        months = ['january', 'february', 'march', 'april', 'may', 'june']  
        month = months.index(month) + 1

    # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
    # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month=df['month'].mode()[0]
    month_dic={1:'January',2:'February',3:'March',4:'April',5:'May',6:'June'}
    com=month_dic.get(most_common_month)
    print('\nMost Common Month is {}'.format(com))
    
    # display the most common day of week
    most_common_day=df['day_of_week'].mode()[0]
    print('\nMost Common Day is {}'.format(most_common_day))
        
    # display the most common start hour
    most_common_hour=df['hour'].mode()[0]
    print('\nMost Common Hour is {}'.format(most_common_hour))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station=df['Start Station'].mode()[0]
    print('\nMost Common Start Station is {}'.format(start_station))
    
    # display most commonly used end station
    end_station=df['End Station'].mode()[0]
    print('\nMost Common End Station is {}'.format(end_station))
    
    # display most frequent combination of start station and end station trip
    df['Trip Road']=df['Start Station']+df['End Station']
    print('\nThe most Frequent Combination of Start Station and End Station is: {} and {}.'.format(start_station,end_station))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print('\nThe Total Travel Time is {} Hours.'.format(round(total_travel_time/3600,2)))
    
    # display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('\nThe Mean Travel Time is {} Minutes.'.format(round(mean_travel_time/60,2)))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types=df['User Type'].value_counts().to_frame()
    print('\nThe user Types Count:\n{}'.format(user_types))
    
    # Display counts of gender
    try:
        gender_count=df['Gender'].value_counts().to_frame()
        print('\nThe Gender Count:\n{}'.format(gender_count))
    except KeyError:
        print('\nThe Gender Data is not available for this City')
    
    # Display earliest, most recent, and most common year of birth
    try:
        earliest_year=df['Birth Year'].min()
        print('\nThe Earliest Year of birth is {}'.format(int(earliest_year)))
    except KeyError:
        print('\nThe Birth Year Data is not available for this city')
    
    try:
        recent_year=df['Birth Year'].max()
        print('\nThe Earliest Year of birth is {}'.format(int(recent_year)))
    except KeyError:
        print('\nThe Birth Year Data is not available for this city')
        
    try:
        most_common_year=df['Birth Year'].mode()
        print('\nThe Earliest Year of birth is {}'.format(int(most_common_year)))
    except KeyError:
        print('\nThe Birth Year Data is not available for this city')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def user_display(df):
    view_data=input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc=0
    while True:
        if view_data=='yes':
            print(df.iloc[int(start_loc):int(start_loc)+5])
            start_loc+=5
            view_data = input("Do you wish to continue?: ").lower()
            continue
        else:
            print('\nNo problem,Choose yes next time if you need to show 5 rows of data')
            break
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        user_display(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
    main()