from openai import OpenAI


client = OpenAI(
    api_key = "sk-None-83q6P8hUUmP09JzQUKgVT3BlbkFJXbhMmfVLLZkkuIsRcNPi"
)

print("Please enter the following promts: \n1. anger \n2. red \n3. Messi \n4. short" + "\n5. played \n6. cars \n7. chicken \n8. unfunny" + "\n9. eating \n10. trash \n11. ID Tech Worker \n12. snake" + "\n13. ugly \n14. caps \n15. lamborghini \n16. Peter \n17. Parker \n")




list_of_words = []
string_of_words = ""

for x in range(17):
    get_input = input("Enter a response to prompt #" + str (x + 1) + ": ")
    list_of_words.append(get_input)

system_data = [
    {"role": "system", "content": "Generate a funny two-paragraph Madlib story using the words."},
    {"role": "user", "content": string_of_words.join(list_of_words)}
]

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages = system_data
)

assistant_response = response.choices[0].message.content
system_data.append({"role": "assistant", "content": assistant_response})
print("Assistant" + assistant_response)
