from elections import *

if __name__ == "__main__":
    e = Election(date(2000, 1, 1))
    f = open("./data/brampton-centre.csv", newline="\n")
    e.read_results(f)
    f = open("./data/labrador.csv", newline="\n")
    e.read_results(f)
    # f = open("./data/medicine-hat.csv", newline="\n")
    # e.read_results(f)
    # f = open("./data/nunavut.csv", newline="\n")
    # e.read_results(f)
    # f = open("./data/parkdale-highpark.csv", newline="\n")
    # e.read_results(f)
    # print(e.riding_winners("Brampton Centre"))
    # print(e.riding_winners("Labrador"))
    print(e.popular_vote())
    # print(e.party_seats())
    # print(e.election_winners())