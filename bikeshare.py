import time
import pandas as pd
import numpy as np
import calendar
import datetime

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
    print('Hello! Let\'s explore some US bikeshare data! \n ')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('The Bikeshare Data of which city do you want to analyze? Please choose from: Chicago, New York City or Washington. \n ').lower()
    # the .lower() makes sure that users can enter in small or capt letters

    while city not in ['chicago', 'new york city', 'washington']:
        # to check if response is valid

                print('Sorry we can only evaluate data for Chicago, New York City or Washington. Please check for correct spelling. \n ')
                city = input('Choose again, which city do you want to analyze: Chicago, New York or Washington? \n ').lower()

    print('Your input was valid we will have a closer look at ' + city + '.\n')

    month = input('Do you want to filter by a specific month? \n If yes you can choose between: January, February, March, April, May or June. \n Otherwise just type: all \n').lower()

    while month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
                print('Sorry we can only filter from january to june or without a specific filter by entering: all. Please check for correct spelling. \n ')
                month = input('Choose again which filter do you want to set? You can choose from january to june or simply: all \n ').lower()

    print('Your input was valid we will have a closer look at ' + city + ' and filter by ' + month + '.\n')

    day = input('Do you want to filter by a specific day? \n Choose the day by typing monday, tuesday, ... Otherwise just type: all.\n').lower()

    while day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
                print('Sorry we can only filter by weekday or without a specific filter by entering: all \n ')
                day = input('Choose again which filter do you want to set? You can type the weekday: monday, tuesday, ... or: all. \n').lower()

    print('Your input was valid we will have a closer look at ' + city + ' filtered by ' + month + ' and ' + day + '.\n')

    print('-'*50)
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
    # here I use the code presented in Practice Problem 3 for loading and filtering the city dataset

        # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Start_hour'] = df['Start Time'].dt.hour # convert start hour into hour

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    #df['month_name'] = df['month'].apply(lambda x:calendar.month_abbr[x])

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

    # TO DO: display the most common month
    common_month = df['day_of_week'].mode().loc[0] # mode to find most common value
    print('The most common month is: ' + common_month + '!\n')
    # month is in the wrong format!

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode().loc[0]
    print('The most common day is: ' + common_day + '!\n')
    # TO DO: display the most common start hour
    common_start_hour = df['Start Time'].mode().loc[0].strftime('%m/%d/%Y')

    print('The most common start hour is: ' + common_start_hour + '!\n')

    print("\nThis calculation took %s seconds." % (time.time() - start_time))

    print('-'*50)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating the most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode().loc[0]
    print('The most common start station is: ' + common_start_station + '!\n')
    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode().loc[0]
    print('The most common start hour is: ' + common_end_station + '!\n')
    # TO DO: display most frequent combination of start station and end station trip
    # Define a new column with string indicating start and end station
    # Then sort for the most common combination
    df['Station Combination'] = df['End Station'] + df['Start Station']
    common_station_combo = df['Station Combination'].mode().loc[0]
    print('The most common trip is: ' + common_station_combo + '!\n')

    print("\nThis calculation took %s seconds." % (time.time() - start_time))
    print('-'*50)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating the Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()/3600
    print('The total travel time is: %d hours!\n' % total_travel_time )

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()/60
    print('The mean travel time is: %d minutes!\n' % mean_travel_time )
    print("\nThis calculation took %s seconds." % (time.time() - start_time))
    print('-'*50)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Statistics...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The user numbers per type are as follows:\n', user_types ,'\n')

    # TO DO: Display counts of gender
    # Gender data is not availbe for all cities thus we need a if condition
    if city in ['chicago', 'new york']:
        gender_types= df['Gender'].value_counts()
        print('The user numbers per gender are as follows:\n', gender_types,'\n')
    else:
        print('For this set there is no gender data available. \n')

    # TO DO: Display earliest, most recent, and most common year of birth
    if city in ['chicago', 'new york']:
        early_byear= df['Birth Year'].min().astype(int)
        print('The most common birth year was:', early_byear,'\n')

        recent_byear= df['Birth Year'].max().astype(int)
        print('The most common birth year was:', recent_byear,'\n')

        common_byear= df['Birth Year'].mode().loc[0].astype(int)
        print('The most common birth year was:', common_byear, '\n')
    else:
        print('For this set there is no birth year data available.')

    print("\nThis calculation took %s seconds." % (time.time() - start_time))
    print('-'*50)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
