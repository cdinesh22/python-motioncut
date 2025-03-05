def count_words(text):
    #SPLITTING
    words=text.split()  
    return len(words)
try:
    #TAKING INPUT
    user_input=input("Enter a sentence/paragraph:: ").strip()
    #ERROR HANDLING
    if not user_input:
        print("Error:Input is empty.Please enter some text.")
    #COUNTING WORDS   
    count= count_words(user_input)
    print(f"Word Count: {count}")
except Exception as e:
    print(f"An ERROR {e}")
