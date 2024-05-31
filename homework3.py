import matplotlib.pyplot as plt

def buchstabe_häufigkeiten(x):
    mein_d = {}
    for buchstabe in x.lower():
        if buchstabe.isalpha():
            if buchstabe not in mein_d:
                mein_d[buchstabe] = 1
            else:
                mein_d[buchstabe] +=1
    mein_d_sorted = dict(sorted(mein_d.items()))
    
    return mein_d_sorted


bh_dict = buchstabe_häufigkeiten(x="123Wie g&eht es Ihnen%?")

plt.bar(bh_dict.keys(), bh_dict.values())                