stopflag = 1


match stopflag:
    case True:
        print("Het systeem gaat aan")
        exit()
    case False:
        print("Het systeem gaat uit")
    case _:
        print("Er is een fout opgetreden")
