import socket

"""
This file defines a class: Assignment2 that implements methods specified in tasks
1. constructor
2. tellAge
3. listAnniversaries
4. modifyYear
5. checkGoodString
6. connectTcp
"""


class Assignment2:
    # Task 1 (Constructor
    def __init__(self, year):
        """
        Constructor that accepts one argument and assigns a class instance variable
        :param year (type int)
        """
        # set the corresponding class instance variable to its initial value.
        self.year = year

    # Task 2 (Age)
    def tellAge(self, currentYear):
        """
        Returns age based on the supplied currentYear argument
        :param currentYear (type int)
        :return str (type str)
        """
        # the age calculation, then print the outcome using standard output.
        print(f"Your age is {currentYear - self.year}")

    # Task 3 (List)
    def listAnniversaries(self):
        """
        Returns a list of all 10-year anniversaries, assuming today is year 2022.
        :return anniversaries (type list)
        """
        # declare a blank list to store the 10-year intervals
        myList = []
        # check from 1 to the difference in years from 2022 for multiples of 10
        for tenth in range(1, 2022 - self.year):
            # if the anniversary criteria is met, add the anniversary to the list of anniversaries.
            if tenth % 10 == 0:
                myList.append(tenth)
        # return the populated list
        return myList

    # Task 4 (String Manipulation)
    def modifyYear(self, n):
        """
        Returns a modified year, fist 2 digits n times followed by the digits at odd positions in year * n
        :param n (type int)
        :return modifiedYearStr (type str)
        """
        currYear = self.year
        # extrapolate the first two characters, then add duplicates of them to the amended year string.
        currStr = str(currYear)[:2] * n
        # get n * year, then stringify it.
        numString = str(currYear * n)
        # append digits in odd positions while looping for the string's length
        for currPos in range(len(numString)):
            # if a digit is found in an odd location, add it to the string.
            if currPos % 2 == 0:
                currStr += numString[currPos]
        # return the expected altered string
        return currStr

    # Task 5 (Loop and Conditional statements)
    @staticmethod
    def checkGoodString(string):
        """
        Returns true if a string is valid, otherwise false
        :param string (type str)
        :return type bool
        """
        # Assign the string to be checked to a variable called "candidateToCheck".
        candidateToCheck = string
        # Set the count of digits in the string to 0.
        countTotalDigits = 0
        # Iterate, through each character "currChar" in the "candidateToCheck" string.
        for currChar in candidateToCheck:
            if (currChar.isdigit()):
                # If the current character is a digit increment the count of digits, by 1.
                countTotalDigits = countTotalDigits + 1
        # If the length of "candidateToCheck" is 9, if it starts with a lowercase letter and contains only one digit.
        return len(candidateToCheck) >= 9 and candidateToCheck[0].islower() and countTotalDigits == 1

    # Task 6 (Socket)
    @staticmethod
    def connectTcp(host, port):

        """
        Returns true if a socket was created and connection to host/port established, otherwise false
        :param host (type str)
        :param port (type int)
        :return type bool
        """
        # use try-catch to handle possible exceptions when establishing connection
        try:
            # Start by creating a socket using the parameters AF_INET. Sock_stream.
            tcpClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Use the socket to establish a connection, with the specified host and port.
            tcpClientSocket.connect((host, port))
            # Once the connection is established, close it.
            tcpClientSocket.close()
            # If no exceptions are thrown during this process return True to indicate that everything was successful.
            return True
        # In case any exceptions occur catch them.
        except Exception as error:
            # Return False instead.
            return False


# run the tests provided in the instructions
def main():
    print("Running checks with provided instructions ...")
    a = Assignment2(2000)
    ret = a.listAnniversaries()
    print(ret)

    a = Assignment2(1991)
    ret = a.listAnniversaries()
    print(ret)

    a = Assignment2(1782)
    ret = a.modifyYear(3)
    print(ret)

    ret = Assignment2.checkGoodString("f1obar0more")
    print(ret)

    ret = Assignment2.checkGoodString("foobar0more")
    print(ret)

    retval = Assignment2.connectTcp("www.google.com", 80)
    if retval:
        print("Connection established correctly")
    else:
        print("Connection error")


if __name__ == '__main__':
    main()
