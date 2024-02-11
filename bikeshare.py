import time
import pandas as pd
import numpy as np

#need to comment
#comment added as requested

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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = str(input('What city would you like to look into? ')).lower()
        if city not in ('chicago','new york city','washington'):
            print('That input is not valid. Please choose from the following: Chicago, New York City, Washington')
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = str(input('Which month(s) would you like to consider? ')).lower()
        if month not in ('all','january','february','march','april','may','june','july','august','september','october','november','december'):
            print('That input is not valid. Please choose either All or one of the 12 months of the year')
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = str(input('Finally, which day(s) of the week would you like to investigate? ')).lower()
        if day not in ('all','monday','tuesday','wednesday','thursday','friday','saturday','sunday'):
            print('That input is not valid. Please choose either All or one of the 7 days of the week')
        else:
            break
    
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
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        
        months = ['january', 'february', 'march', 'april', 'may', 'june','july','august','september','october','november','december']
        month = months.index(month) + 1
    
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
           
    return df

def time_stats(df):
    """Takes a DataFrame and computes the most common (mode) month, day and hour of travel"""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    df['month'] = df['Start Time'].dt.month


    popular_month = df['month'].mode()[0]
    months=['january','february', 'march', 'april', 'may', 'june','july','august','september','october','november','december']
    pop_month=months[popular_month-1]
    
    print('Most Popular Start Month:', pop_month.title())

    # TO DO: display the most common day of week

    df['day_of_week'] = df['Start Time'].dt.weekday_name


    popular_day_of_week = df['day_of_week'].mode()[0]
    
    print('Most Popular Start Day:', popular_day_of_week)

    # TO DO: display the most common start hour


    df['hour'] = df['Start Time'].dt.hour

    popular_hour = df['hour'].mode()[0]
    
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Takes a DataFrame and computes the most popular (mode) start station, end station and combination of start and end stations."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    popular_start_station = df['Start Station'].mode()[0]
    
    print('Most Popular Start Station:', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    
    print('Most Popular End Station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Start and End'] = 'Starting at ' +df['Start Station'] +' and ending at '+ df['End Station']
    
    popular_start_and_end = df['Start and End'].mode()[0]
    
    print('Most Popular Start and End:', popular_start_and_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel=df['Trip Duration'].sum()
    days=total_travel//(86400)
    hours=(total_travel-86400*days)//3600
    minutes=(total_travel-86400*days-3600*hours)//60
    seconds=(total_travel-86400*days-3600*hours-60*minutes)
    print('Total Travel Time:',int(days),'days,',int(hours),'hours,',int(minutes),'minutes, and',int(round(seconds)),'seconds')
    
    # TO DO: display mean travel time
    mean_travel=df['Trip Duration'].mean()
    days=mean_travel//(86400)
    hours=(mean_travel-86400*days)//3600
    minutes=(mean_travel-86400*days-3600*hours)//60
    seconds=(mean_travel-86400*days-3600*hours-60*minutes)
    print('Mean Travel Time:',int(days),'days,',int(hours),'hours,',int(minutes),'minutes, and',int(round(seconds)),'seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print(gender)
    except:
        print('Gender data is not included for your chosen city')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        early=df['Birth Year'].min()
        latest=df['Birth Year'].max()
        common=df['Birth Year'].mode()[0]
        print('Earliest birth year:',int(early),'\nLatest birth year:',int(latest),'\nMost common birth year:',int(common))
    except:
        print('Birth year data is not included for your chosen city')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def rawdata(df):
    view_data = input("Would you like to view the first 5 rows of trip data for your selection? Enter yes or no? ").lower()
    if view_data == 'yes':
        start_loc = 0
        view_display=view_data
        while view_display.lower()=='yes' and start_loc+5<df.shape[0]:
            print(df.iloc[start_loc:start_loc+5])
            start_loc += 5
            view_display = input("Do you wish to continue?: ")
    if view_data == 'no':
        print('No problem')

        

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        rawdata(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
