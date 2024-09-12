movie_time_min: int = int(input("Enter length of the movie in minutes :"))
houer: int = int(movie_time_min / 60)
minute: int = movie_time_min % 60
print(f"houer : {houer}  minute : {minute}" )