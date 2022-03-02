def printrangoli(size):
    n=size
    l = list(map(chr,range(97,123)))        # Creats a List of Aplhabets by providing the ASCII numbers of char in the "chr" function
    w  = len("-".join(l[n-1::-1]+l[1:n]))   # The width of the whole Pattern is w=equal to the center/mid line.

    # The below  loop prints the Top as well as bottom line

    for i in range(1,n):
        print(
            ("-".join(              #Joins the alphabets with "-" character
                l[n-1:n-i:-1]       #Prints the Top Left Part
                +
                l[n-i:n]))          # Prints the Top Right Part
                .center(w ,"-")     # Center justifies the Top Pattern
            )

    # The Below loop prints the Bottom Part

    for i in range(n,0,-1):
        print((("-".join(l[n-1:n-i:-1] + l[n-i:n])).center(w ,"-")) )

size = int(input())
printrangoli(size)


# --------   e--------
# ------e-   d-e------
# ----e-d-   c-d-e----
# --e-d-c-   b-c-d-e--

# e-d-c-b-   a-b-c-d-e
# --e-d-c-   b-c-d-e--
# ----e-d-   c-d-e----
# ------e-   d-e------
# --------   e--------