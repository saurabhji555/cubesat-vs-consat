from sklearn.linear_model import LogisticRegression

# Sample training data
X = [[0.2], [0.6], [0.8], [0.4], [0.9]]
y = [1, 1, 0, 1, 0]  # 1 = Good route, 0 = Avoid

model = LogisticRegression()
model.fit(X, y)

# Predict for new satellite load
new_bandwidth = [[0.5]]
if model.predict(new_bandwidth)[0] == 1:
    print("✅ Route traffic via this satellite")
else:
    print("❌ Avoid route, overloaded")
