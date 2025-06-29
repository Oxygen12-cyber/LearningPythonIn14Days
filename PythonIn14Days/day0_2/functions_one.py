while True:
    def combineNames( firstName, lastName, message='hello',):
        combined = firstName + " " + lastName

        print(f'{message} {combined}')

    combineNames(input('your firstname '), input('your lastname '))