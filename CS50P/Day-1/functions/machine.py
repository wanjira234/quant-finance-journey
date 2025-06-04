emoticon = "^_^"

def main():
    global emoticon
    say("Anyone there? ")
    emoticon = ":D"
    say('oh, hi')
def say(phrase):
    print(phrase + " " + emoticon)

main()