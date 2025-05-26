{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "84d833b1-66da-45e7-b4ed-88e2a7743648",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.metrics import confusion_matrix, classification_report, roc_auc_score\n",
    "\n",
    "def evaluate_model(model, X_test, y_test):\n",
    "    y_pred = model.predict(X_test)\n",
    "    print(confusion_matrix(y_test, y_pred))\n",
    "    print(classification_report(y_test, y_pred))\n",
    "    auc = roc_auc_score(y_test, model.predict_proba(X_test)[:,1])\n",
    "    print(f\"AUC: {auc}\")\n",
    "    return auc\n"
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
