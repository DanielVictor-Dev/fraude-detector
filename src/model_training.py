{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c3e79fdd-260d-4fce-a088-37a9a176cf15",
   "metadata": {},
   "outputs": [],
   "source": [
    "import joblib\n",
    "from xgboost import XGBClassifier\n",
    "\n",
    "def train_model(X_train, y_train):\n",
    "    model = XGBClassifier()\n",
    "    model.fit(X_train, y_train)\n",
    "    return model\n",
    "\n",
    "def save_model(model, path):\n",
    "    joblib.dump(model, path)\n",
    "\n",
    "def load_model(path):\n",
    "    return joblib.load(path)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
