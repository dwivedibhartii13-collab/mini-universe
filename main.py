import openai


openai.api_key = "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" 

print("Welcome to your Mini-Universe!")
name = input("Enter your name: ")


print("\nRate yourself from 1-5:")
curiosity = int(input("Curiosity: "))
bravery = int(input("Bravery: "))
kindness = int(input("Kindness: "))


interests = input("List your top 3 interests (comma-separated): ")

user_profile = {
    "name": name,
    "curiosity": curiosity,
    "bravery": bravery,
    "kindness": kindness,
    "interests": interests
}


def generate_scenario(profile):
    """
    Uses OpenAI GPT to generate a starting scenario in the mini-universe.
    """
    prompt = f"""
    You are creating a small text-based universe for a user.
    User Profile: {profile}
    
    Generate a short scenario (3-5 sentences) for the user in their mini-universe.
    Include 2 choices for the user to make.
    Make the scenario reflect their traits and interests.
    Format:
    Scenario: <text>
    Choices:
    1. <option1>
    2. <option2>
    """
    response = openai.ChatCompletion.create(
        model="gpt-5-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8
    )
    return response['choices'][0]['message']['content']


scenario_text = generate_scenario(user_profile)
print("\n--- Your Mini-Universe Scenario ---\n")
print(scenario_text)



choice = input("\nWhich choice do you pick? (1 or 2): ")


def generate_consequence(profile, previous_scenario, choice):
    """
    Generates the consequence of the user's choice in the mini-universe.
    """
    prompt = f"""
    User Profile: {profile}
    Previous Scenario: {previous_scenario}
    User Choice: {choice}
    
    Describe what happens next in the mini-universe (3-5 sentences).
    Include how the user's traits influence the outcome.
    """
    response = openai.ChatCompletion.create(
        model="gpt-5-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8
    )
    return response['choices'][0]['message']['content']


consequence_text = generate_consequence(user_profile, scenario_text, choice)
print("\n--- Consequence of Your Choice ---\n")
print(consequence_text)

print("\nThis is just the start of your mini-universe. You can expand it with more choices and scenarios!")
