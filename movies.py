"""
Python Summative Assessment 1 [9-12.CT.d]
Zelem Tuguldur
"""
#import modules to validate the time and number
import datetime
import re
#Tuples with the movies and times
movies = ('Lego Movie', 'Shrek', 'Midway')
periods = ('Morning', 'Afternoon','Evening')

time_choice = None
movie_choice = None
period_choice = None

#list of booked seats
ordered_seats = []
for movie in movies:
    ordered_seats.append(([], [], []))

#Print movies and book movies

def pick_movie(movies):

    print ()
    print ('Todays Movies')
    print ('-------------')
    for index, movie in enumerate(movies):
        print (f"{index + 1}. {movie}")
    
    #Add a blank line
    print()
    
    #Select movie
    #validate movie choice with input
    movie_choice = None
    while movie_choice == None:
        movie_choice = input ('Please, enter the movie code: ')
        try:
            movie_choice = int(movie_choice)
            if movie_choice not in range(1, len(movies) + 1):
                movie_choice = None
        except:
            movie_choice = None
    return movie_choice - 1

#time picking function
def pick_time(periods):
    
    print()
    print("Movie time periods")
    print ('-------------')
    for index, period in enumerate(periods):
        print (f"{index + 1}. {period}")
    print()
    
    period_choice = None
    while period_choice == None:
        period_choice = input("Please select a time period: ")
        try:
            period_choice = int(period_choice)
            if period_choice not in range(1, 4):
                period_choice = None
        except:
            period_choice = None
    return period_choice - 1

#Seat picking function
def pick_seat(movie_index, period_index, ordered_seats):
    seats_txt = ''
    
    print()
    print('Pick your seat')
    print('--------------')
    for seat in range(1,16):
        if seat in ordered_seats[movie_index][period_index]:
            seats_txt = seats_txt + ' xx'
        else:
            seats_txt = seats_txt + ' {:02d}'.format(seat)
        if seat % 5 == 0:
            seats_txt = seats_txt + '\n'
    print (seats_txt)
    
    seat_choice = None
    while seat_choice not in range(1, 16):
        try:
            seat_choice = int(input("Please select the seat you want: "))
        except:
            print("Please enter a valid seat number")
            continue
        if seat_choice not in range(1, 16) or seat_choice in ordered_seats[movie_index][period_index]:
            print("Seat not available, choose a different seat")
            seat_choice = None
        else:
            ordered_seats[movie_index][period_index].append(seat_choice)
            print(f"Seat {seat_choice} booked")
    
    return seat_choice

#Cancel seat order
def repeal_seats(movie_index, period_index, ordered_seats, seat_choice):
    ordered_seats[movie_index][period_index].remove(seat_choice)
    print("Your order has been canceled")

#Beginning of bot
print("Welcome to Zaisan Hill Movie Ordering Bot")

name = input('Please enter your name: ')
valid_number = None

#phone validation
while valid_number == None:
    phone_number = input("Please enter your phone number: ")
    valid_number = re.match(r'^([\s\d]+)$', phone_number)

#ask if they want to rebook
rebook = 'yes'

while rebook == 'yes':
    movie_choice = pick_movie(movies)
    period_choice = pick_time(periods)
    seat_choice = pick_seat(movie_choice, period_choice, ordered_seats)
    #Display order information
    print(f"Name: {name}, Phone: {phone_number}, Movie: {movies[movie_choice]}, Period: {periods[period_choice]}")
    
    correct = None
    #Check if information is correct
    while correct not in ('yes', 'no'):
        correct = (input("Is the above information correct? ")).lower()
        if correct == 'yes':
            print('Thank you for your order.')
        elif correct == 'no':
            repeal_seats(movie_choice, period_choice, ordered_seats, seat_choice)
    
    rebook = None
    
    while rebook not in ('yes', 'no'):
        rebook = (input("Would you like to rebook your order? ")).lower()
        if rebook == 'yes':
            print('Rebooking...')
        elif rebook == 'no':
            print("Thank you, choose us again!")


