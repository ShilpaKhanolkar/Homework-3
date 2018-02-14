file_no=['1','2']
print("------------------")
print("Paragraph Analysis")
print("------------------")
for num in file_no:
    with open("raw_data/paragraph_" + num + ".txt") as file:
        
        print()
        print("For Paragraph" + str(num))
        
        # Import a text file filled with a paragraph of your choosing.
        para = file.read()

        # Assess the passage for each of the following:

        # Approximate word count
        word_array = para.split(' ')
        word_count = len(word_array)
        print("Approximate word count: " + str(word_count))


        # Approximate sentence count
        sentence_array = para.split('.')
        sentence_count = len(sentence_array) -1 # -1 to delete the last split's 2nd portion
        print("Approximate sentence count: " + str(sentence_count))
    
        # Approximate letter count (per word)
        letter_array = para.split()
        # remove white spaces in the array
        # remove commas and periods
        # remove any other non-letter char
        # NOTE: loop through this array and remove the above char (for loop)
        # or loop through this array and push letter characters to a new array
        letter_count = 0
        for letter in para:
            if letter == ' ' or letter == ',' or letter == '.' or letter == '(' or letter == ')' or letter == '>' or letter == '\'' or letter == '\"':
                letter_count = letter_count
            else:
                letter_count = letter_count + 1
        letter_count_perword = round((letter_count/word_count),2)
        #print("Letter count: " + str(letter_count))
        print("Approximate letter count (per word): " + str(letter_count_perword))

        # Average sentence length (in words)
        avg_sentence_length = round((word_count/sentence_count),2)
        print("Average sentence length (in words): " + str(avg_sentence_length))






