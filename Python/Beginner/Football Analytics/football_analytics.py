import requests
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Collect data from an online API
def collect_data():
    # Replace with your API key from football-data.org
    headers = {"X-Auth-Token": "4ac71c6e73234453821358d2e64241a2"}
    url = "https://api.football-data.org/v2/matches"
    
    # Request the data from the API
    response = requests.get(url, headers=headers)
    
    # Debugging: print the raw JSON response to inspect its structure
    print(response.json())  # This will help check the structure of the response
    
    # Check if the response contains 'matches'
    data = response.json()
    if 'matches' not in data:
        print("Error: 'matches' key not found in the response.")
        return pd.DataFrame()  # Return an empty DataFrame to avoid further errors
    
    matches = []
    
    # Parse the matches from the response
    for match in data['matches']:
        home_team = match['homeTeam']['name']
        away_team = match['awayTeam']['name']
        outcome = match['score']['winner']
        
        if outcome == "HOME_TEAM":
            outcome = 'HOME_WIN'
        elif outcome == "AWAY_TEAM":
            outcome = 'AWAY_WIN'
        elif outcome == "DRAW":
            outcome = 'DRAW'
        
        matches.append([home_team, away_team, outcome])
    
    # Convert the data to a DataFrame
    matches_df = pd.DataFrame(matches, columns=["Home Team", "Away Team", "Outcome"])
    return matches_df

# Train a model to predict match outcomes
def train_model(matches_df):
    # Prepare data for training
    matches_df['Outcome'] = matches_df['Outcome'].map({'HOME_WIN': 1, 'AWAY_WIN': 2, 'DRAW': 0})
    
    X = matches_df[['Home Team', 'Away Team']]  # Features: Home and Away teams
    y = matches_df['Outcome']  # Target: Outcome
    
    # Convert categorical data (team names) into numerical values
    X = pd.get_dummies(X)
    
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize and train the model
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy * 100:.2f}%")
    
    return model

# Main Menu function
def main_menu():
    # Welcome message
    print("\nWelcome to the Football Analytics Project!")
    
    # Display options
    print("1. Collect and Analyze Match Data")
    print("2. Exit")
    
    choice = input("Choose an option (1-2): ")
    
    if choice == '1':
        matches_df = collect_data()
        if not matches_df.empty:
            model = train_model(matches_df)
    elif choice == '2':
        print("Exiting program. Goodbye!")
        return
    else:
        print("Invalid choice. Please try again.")
        main_menu()

# Main function to run the program
def main():
    main_menu()

# Run the program
if __name__ == "__main__":
    main()
