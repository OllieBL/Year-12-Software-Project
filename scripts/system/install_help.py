import pickle

with open('scripts/system/login_details.txt', 'wb') as f:
    pickle.dump([['','',0]], f)