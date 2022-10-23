stopflag = True


match stopflag:
    case True:
        print("Het systeem gaat uit")
        exit()
    case False:
        print("Het systeem gaat uit")
    case _:
        print("Er is een fout opgetreden")
