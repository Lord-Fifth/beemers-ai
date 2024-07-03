from openai import OpenAI

# Set up your OpenAI API key

def generate_spending_insights(transaction_history):
    # Prepare the prompt with user's transaction history
    prompt = f"Provide personalized spending insights and budgeting advice based on the following transaction history: {transaction_history}"
    client = OpenAI(
    api_key='xxxxx'
    )
    # Call the OpenAI API using the updated method
    response = client.chat.completions.create(
        model="gpt-4",  # Use an appropriate model
        messages=[
            {"role": "user", "content": prompt}
        ]
        # max_tokens=200
    )

    # Extract the insights from the response
    insights = response.choices[0].message
    return insights

# Example transaction history
transaction_history = """
- $50 on groceries
- $20 on transportation
- $100 on dining out
- $30 on entertainment
"""

# Get personalized insights
insights = generate_spending_insights(transaction_history)
print(insights)

# def recommend_payment_method(user_data):
#     # Prepare the prompt with user's data
#     prompt = f"Based on the following user data, recommend the best payment method and time for making payments: {user_data}"

#     # Call the OpenAI API
#     response = openai.Completion.create(
#         engine="text-davinci-003",
#         prompt=prompt,
#         max_tokens=150
#     )

#     # Extract the recommendation from the response
#     recommendation = response.choices[0].text.strip()
#     return recommendation

# # Example user data
# user_data = """
# - Frequent small transactions during weekdays
# - Larger transactions on weekends
# - Prefers credit card over debit card
# """

# # Get payment recommendations
# recommendation = recommend_payment_method(user_data)
# print(recommendation)

# def detect_fraud(transaction):
#     # Prepare the prompt with transaction details
#     prompt = f"Analyze the following transaction and determine if it is potentially fraudulent: {transaction}"

#     # Call the OpenAI API
#     response = openai.Completion.create(
#         engine="text-davinci-003",
#         prompt=prompt,
#         max_tokens=100
#     )

#     # Extract the fraud detection result from the response
#     result = response.choices[0].text.strip()
#     return result

# # Example transaction
# transaction = """
# - Amount: $5000
# - Location: New York
# - Time: 2:00 AM
# - User's usual spending pattern: small amounts during the day
# """

# # Check for fraud
# fraud_detection_result = detect_fraud(transaction)
# print(fraud_detection_result)

