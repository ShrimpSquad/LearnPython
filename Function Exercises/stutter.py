# Define a function that makes it sound as if it were stuttering.
# e.g. "What do you mean?" --> "W.. W.. What do you mean?"

def stutter(string):
    return f"{string[0]}.. {string[0]}.. {string}"

print(stutter("What do you mean?"))