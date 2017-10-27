import media
import freshtomatoes


toystory = media.Movie("Toy story","A story of boy and his toys thata come to life","http://0.media.dorkly.cvcdn.com/93/37/6af85e48981ebe35c3cda962730853b7.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc")
ring = media.Movie("Ring","A story of boy and his toys thata come to life","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRzrDBEEMpAroabuJpjhrzjXuadjZru_JH5KQ8JXSDepSeh1IjU","https://www.youtube.com/watch?v=uukQ_6szDm8")
Titanic = media.Movie("Titanic","A story of boy and his toys thata come to life","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRH9gvhgrItbyhr_584zX_qdDGumLO1h5zuw-AzasrpdNjkmrnF9A","https://www.youtube.com/watch?v=ZQ6klONCq4s")
avatar  = media.Movie("Avatar","A marine on an alien planet","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSnPP5bZoelxP7HsykwgpN0ioAb7tcLWDhuq5Sqz6rLv5RPsqTZ4w","https://www.youtube.com/watch?v=5PSNL1qE6VY")
school_of_rock = media.Movie("School of rock","Using rock to learn music","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR2W9Tnro_L4MhPS2eb6pWhcsPnXU73CeKEcvKaL2GUypkJDmKFUg","https://www.youtube.com/watch?v=5afGGGsxvEA")
movies = [toystory,ring,Titanic,avatar,school_of_rock]
print(media.Movie.__doc__)
freshtomatoes.open_movies_page(movies)