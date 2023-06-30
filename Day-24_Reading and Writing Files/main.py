# READ OPERATION
with open("my_file.txt") as file:
    file_contents = file.read()
    # print(file_contents)

with open("my_file.txt", "r") as file:
    print(file.readlines())

with open("new_file.txt", "r") as file:
    print(file.readlines(17))

# WRITE OPERATION
# with open('my_file.txt', mode='a', encoding='utf-8') as file:
#     file.write("""\nNow, that we are surrounded with so great a cloud of witnesses,
#     Cheering us on. Cheering us on.
#     Let us run the course set before us, looking unto JESUS, the AUTHOR and FINISHER
#     of our faith.
# """)

# mode='w' can be used to create new file
# with open('new_file.txt', mode='w', encoding='utf-8') as file:
#     file.write("""Ephesians 4:1-6:
# As a prisoner for the Lord, then, I urge you to
# live a life worthy of the calling you have received.
# Be completely humble and gentle; be patient, bearing with one another in love.
# Make every effort to keep the unity of the Spirit through the bond of peace.
# There is one body and one Spirit, just as you were called to one hope when you were called;
# one Lord, one faith, one baptism; one God and Father of all, who is over all and through all and in all.
# """)
