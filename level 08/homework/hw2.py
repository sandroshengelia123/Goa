# 2) შექმენით პროგრამა რომელსაც შეეძლება დიალოგი თქვენგან (აირჩიეთ ნებისმიერი თემა)

print("pick one of the includded hobbies:")
hobby = input("programing, gaming, guitar, and sing")

if hobby == "proggraming":
    print("I love" , hobby + ",")
    language = input("what is your programming language")
    print(language, "is such a great programming language")


elif hobby == "gaming":
    print("I love" , hobby + ",")
    fav_game = input("what is your favorite game")
    print("I also love", fav_game + "I", "we should play it together")


elif hobby == "music":
    print("I love" , hobby + ",")
    fav_game = input("what is your favorite band")
    print("hell yea", "we should go to a", "fav_band," "concert!")


else:
    print("I love" , hobby + ",")
    fav_artist = input("whom is your favorite band?")
    print("interesting, I have seen,")(fav_artist + "s", "Art, they are solid")
