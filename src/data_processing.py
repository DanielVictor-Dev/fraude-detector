{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "455207b0-136b-4ed9-bd31-575798b768ff",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from sklearn.preprocessing import StandardScaler\n",
    "\n",
    "def load_data(filepath):\n",
    "    return pd.read_csv(filepath)\n",
    "\n",
    "def preprocess_data(df):\n",
    "    scaler = StandardScaler()\n",
    "    df_scaled = scaler.fit_transform(df)\n",
    "    return df_scaled, scaler\n"
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
