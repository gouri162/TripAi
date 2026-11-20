# import requests
# import pandas as pd
# from sklearn.linear_model import LogisticRegression


# url = "https://travel-advisor.p.rapidapi.com/hotels/list"

# headers = {
#     "X-RapidAPI-Key": "126fcf50a5msh224d130318e8259p1fd10fjsn8281382231b7",
#     "X-RapidAPI-Host": "travel-advisor.p.rapidapi.com"
# }

# params = {
#     "location_id": "293919" 
# }

# response = requests.get(url, headers=headers, params=params)
# data = response.json() #Api data name 
 
# # step 2 train krre hai data model ko
# dataset = {
#     "price": [50, 80, 120, 200, 300, 60, 90, 250],
#     "rating": [3.5, 4.0, 4.2, 4.5, 5.0, 3.8, 4.1, 4.8],
#     "cheap":  [1,   1,   1,   0,   0,   1,   1,   0]
# }

# df = pd.DataFrame(dataset)

# X = df[["price", "rating"]]
# y = df["cheap"]

# model = LogisticRegression()
# model.fit(X, y)

# # processing API data 
# hotels = data.get("data", [])

# print("\n===== HOTEL RESULTS =====\n")

# for hotel in hotels[:5]:  # top 5 hotels

#     try:
#         name = hotel.get("name", "N/A")

#         # clean price
#         price_str = hotel.get("price", "")
#         price = int(''.join(filter(str.isdigit, price_str))) if price_str else 0

#         # clean rating
#         rating_str = hotel.get("rating", "0")
#         rating = float(rating_str)

#         if price == 0 or rating == 0:
#             continue

#         # -------------------------------
#         # STEP 4: ML PREDICTION
#         # -------------------------------
#         input_df = pd.DataFrame([[price, rating]], columns=["price", "rating"])
#         prediction = model.predict(input_df)

#         result = "Cheap" if prediction[0] == 1 else "Expensive"

#         # -------------------------------
#         # STEP 5: OUTPUT
#         # -------------------------------
#         print(f"Hotel: {name}")
#         print(f"Price: {price}")
#         print(f"Rating: {rating}")
#         print(f"Prediction: {result}")
#         print("----------------------")

#     except Exception as e:
#         continue
import requests
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# ==========================================
# STEP 1: API CONFIG
# ==========================================

url = "https://travel-advisor.p.rapidapi.com/hotels/list"

headers = {
    "X-RapidAPI-Key": "126fcf50a5msh224d130318e8259p1fd10fjsn8281382231b7",
    "X-RapidAPI-Host": "travel-advisor.p.rapidapi.com"
}

# DELHI LOCATION ID
params = {
    "location_id": "304551",
    "adults": "1",
    "rooms": "1",
    "nights": "2",
    "offset": "0",
    "currency": "USD",
    "order": "asc",
    "limit": "30",
    "sort": "recommended",
    "lang": "en_US"
}

# ==========================================
# STEP 2: API REQUEST
# ==========================================

print("\nFetching hotel data...\n")

response = requests.get(url, headers=headers, params=params)

print("Status Code:", response.status_code)

# check request success
if response.status_code != 200:
    print("API Request Failed!")
    print(response.text)
    exit()

data = response.json()

# DEBUG OUTPUT
print("\nAPI Response Received\n")

# ==========================================
# STEP 3: EXTRACT HOTEL DATA
# ==========================================

hotels = data.get("data", [])

print("Hotels Fetched:", len(hotels))

# safety check
if len(hotels) == 0:
    print("\nNo hotels returned from API.")
    print(data)
    exit()

# ==========================================
# STEP 4: CREATE TRAINING DATA
# ==========================================

training_data = []

for hotel in hotels:

    try:

        name = hotel.get("name", "N/A")

        # --------------------------
        # CLEAN PRICE
        # --------------------------

        price_str = hotel.get("price", "")

        price_digits = ''.join(filter(str.isdigit, price_str))

        if price_digits == "":
            continue

        price = int(price_digits)

        # --------------------------
        # CLEAN RATING
        # --------------------------

        rating_str = hotel.get("rating", "0")

        rating = float(rating_str)

        # skip invalid values
        if price == 0 or rating == 0:
            continue

        # --------------------------
        # CREATE LABEL
        # cheap = 1
        # expensive = 0
        # --------------------------

        cheap = 1 if price < 15000 else 0

        # store row
        training_data.append([price, rating, cheap])

    except Exception as e:
        continue

# ==========================================
# STEP 5: DATAFRAME
# ==========================================

df = pd.DataFrame(
    training_data,
    columns=["price", "rating", "cheap"]
)

print("\nDataset Created Successfully!\n")

print(df.head())

# safety check
if len(df) < 5:
    print("\nNot enough training data!")
    exit()

# ==========================================
# STEP 6: FEATURES & LABELS
# ==========================================

X = df[["price", "rating"]]

y = df["cheap"]

# ==========================================
# STEP 7: TRAIN TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ==========================================
# STEP 8: TRAIN MODEL
# ==========================================

model = LogisticRegression()

model.fit(X_train, y_train)

print("\nModel Trained Successfully!")

# ==========================================
# STEP 9: MODEL ACCURACY
# ==========================================

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("\nModel Accuracy:", round(accuracy * 100, 2), "%")

# ==========================================
# STEP 10: HOTEL PREDICTIONS
# ==========================================

print("\n========== HOTEL PREDICTIONS ==========\n")

for hotel in hotels[:10]:

    try:

        name = hotel.get("name", "N/A")

        # price cleaning
        price_str = hotel.get("price", "")

        price_digits = ''.join(filter(str.isdigit, price_str))

        if price_digits == "":
            continue

        price = int(price_digits)

        # rating cleaning
        rating_str = hotel.get("rating", "0")

        rating = float(rating_str)

        if price == 0 or rating == 0:
            continue

        # prediction input
        input_df = pd.DataFrame(
            [[price, rating]],
            columns=["price", "rating"]
        )

        prediction = model.predict(input_df)

        result = "Cheap Hotel" if prediction[0] == 1 else "Expensive Hotel"

        # ==================================
        # OUTPUT
        # ==================================

        print("Hotel Name:", name)
        print("Price:", price)
        print("Rating:", rating)
        print("Prediction:", result)
        print("-----------------------------------")

    except Exception as e:
        continue