# 21-04 Feature scaling
import numpy as np
import pandas as pd
from sklearn.datasets import load_diabetes, load_wine
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler, StandardScaler

pd.set_option("display.width", 120)

# Example 1: features on very different scales
wine = load_wine(as_frame=True)
print(wine.data[["alcohol", "malic_acid", "magnesium", "proline"]].describe().loc[["mean", "std", "min", "max"]].round(2))

# Example 2: StandardScaler - mean 0, standard deviation 1
X_train, X_test, y_train, y_test = train_test_split(
    wine.data, wine.target, test_size=0.25, random_state=42, stratify=wine.target
)
scaler = StandardScaler().fit(X_train)
print(np.round(scaler.mean_[:3], 3), np.round(scaler.scale_[:3], 3))
X_train_std = scaler.transform(X_train)
print(np.round(X_train_std.mean(axis=0)[:3], 6), np.round(X_train_std.std(axis=0)[:3], 6))

# Example 3: MinMaxScaler - squeeze every feature into 0 to 1
minmax = MinMaxScaler().fit(X_train)
X_train_mm = minmax.transform(X_train)
print(X_train_mm.min(axis=0)[:3], X_train_mm.max(axis=0)[:3])

# Example 4: the test set is transformed with the TRAINING statistics
X_test_mm = minmax.transform(X_test)
print(np.round(X_test_mm.min(axis=0)[:3], 3), np.round(X_test_mm.max(axis=0)[:3], 3))

# Example 5: scaling transforms distance-based models
for name, train, test in [
    ("unscaled", X_train, X_test),
    ("standardised", X_train_std, scaler.transform(X_test)),
    ("min-max", X_train_mm, X_test_mm),
]:
    knn = KNeighborsClassifier().fit(train, y_train)
    print(f"{name:<13} k-NN test accuracy {knn.score(test, y_test):.3f}")

# Example 6: which features dominate the distances without scaling?
gap = (X_train.max() - X_train.min()).sort_values(ascending=False)
print(gap.head(3).round(1))

# Example 7: scaling makes regularised coefficients comparable
diabetes = load_diabetes(as_frame=True, scaled=False)
Xd_train, Xd_test, yd_train, yd_test = train_test_split(diabetes.data, diabetes.target, test_size=0.25, random_state=42)
raw = Ridge(alpha=1.0).fit(Xd_train, yd_train)
scaled = StandardScaler().fit(Xd_train)
std = Ridge(alpha=1.0).fit(scaled.transform(Xd_train), yd_train)
print(pd.DataFrame({"raw": raw.coef_, "standardised": std.coef_}, index=diabetes.data.columns).round(2).head(4))

# Example 8: inverse_transform maps scaled values back to the original units
print(np.round(scaler.inverse_transform(X_train_std[:1])[0][:3], 2), X_train.iloc[0, :3].tolist())
