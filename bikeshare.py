import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Which city would you like to explore ?")
        city = city.lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print("invalid input. Please enter a valid input :")
    # get user input for month (all, january, february, ... , june)
    while True:    
        month = input("Do you want details specific to a particular month? If yes, type month name from within first six months else type 'all'")
        month = month.lower()
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            break
        else:
            print("invalid input. Please enter a valid input :")
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Do you want details specific to a particular day? If yes, type day name else type 'all'")
        day = day.lower()
        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            break
        else:
            print("invalid input. Please enter a valid input")
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
        df - pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
    
        # filter by month to create the new dataframe
        df = df[df['month']==month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']==day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
  
    print('most_common_month',df['Start Time'].dt.month.mode()[0], '\n')


    # TO DO: display the most common day of week
    print('most_common_day_of_week:',df['Start Time'].dt.day_name().mode()[0],'\n')


    # TO DO: display the most common start hour
    
    print('most_common_start_hour:',df['Start Time'].dt.hour.mode()[0],'\n')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('most commonly used start station: ',df['Start Station'].mode()[0],'\n')


    # TO DO: display most commonly used end station
    
    print('most commonly used end station: ',df['End Station'].mode()[0],'\n')


    # TO DO: display most frequent combination of start station and end station trip
    
    df['Combination']= df['Start Station']+ ' '+ df['End Station'] 
    
    print('most frequent combination of start station and end station trip:', df['Combination'].mode()[0],'\n')
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('total travel time', df['Trip Duration'].sum(),'\n')


    # TO DO: display mean travel time
    print('mean travel time', df['Trip Duration'].mean(),'\n')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('counts of user types', df['User Type'].value_counts(),'\n')


    # TO DO: Display counts of gender
    
    print('counts of gender', df['Gender'].value_counts(),'\n')


    # TO DO: Display earliest, most recent, and most common year of birth
    
    print('earliest year of birth', df['Birth Year'].min(),'\n')
    print('most recent year of birth', df['Birth Year'].max(),'\n')
    print('most common year of birth', df['Birth Year'].mode()[0],'\n')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    x = 1
    while True:
        raw = input('\nWould you like to see some raw data? Enter yes or press any key. \n')
        if raw.lower() == 'yes':
            print(df[x:x+5])
            x = x+5
        else:
            break

   # added comment to check git branching 
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
