# TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0] 
    print("Most common day of week is: ", most_common_day)

    # TO DO: display the most common start hour
    most_common_hour = df['hour'].mode()[0] 
    print("Most common Start Time is: ", most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print("Most commonly used start station is: ",most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print("Most commonly used end station is: ",most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    """ We will use gruop by to combinde start and end station but we can't use mode() then we use sort values and shows the first number of the row using head(1) """
    combine_stations = df.groupby(['Start Station','End Station'])
    most_combine_stations =  combine_stations.size().sort_values(ascending = False).head(1)
    print('most frequent combination of start station and end station trip is: ',most_combine_stations)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('the total travel time is: ',total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('the mean travel time is: ',mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    print('the count of user types are: ' , df['User Type'].value_counts() ) 
    
    # TO DO: Display counts of gender
    
    """ we must check the city from user input that isn't have city name washington because doesn't have a coloumns of     genders and year of the birth """

    if city != 'washington':
        print('the count of genders are: ' , df['Gender'].value_counts() )

    # TO DO: Display earliest, most recent, and most common year of birth
    print('the earliest year is: ' , df['Birth Year'].min() )
    print('the recent year is: ' , df['Birth Year'].max() )
    print('the most common year is: ' , df['Birth Year'].mode()[0] )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
  

# view raw data
def show_row_data(df):
    row = 0
    while True:
        view_raw_data = input("would you like see the raw data? if yes Enter 'Y' if no Enter 'N'.\n").lower() 
        if view_raw_data == "y":
            print( df.iloc[ row : row + 6] )
            row += 6
        elif view_raw_data == "n":
            break
        else:
            print(" sorry you enter wrong Input , try again")
            
        


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        show_row_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if name == "main":
  main()
