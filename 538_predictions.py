import requests
import scipy.stats
import csv

# get madness.json
r = requests.get('https://projects.fivethirtyeight.com/march-madness-api/2016/madness.json', verify=False)
json = r.json()

# get the games portion of the data
games = json['games']['mens']
win_probability_master = {}

# for each game
for i in range(len(games)-1):

    # get snapshots
    times = games[i]['winprobs']

    # determine winner
    first_win = False
    last = times[-1]
    if last[4] == 1.0:
        first_win = True

    # for each snapshot, add to master
    for time in times:

        # get the win probability at the given snapshot
        # cut it off at 2 decimal points so we can amass a meaningful sample size
        time[4] = round(time[4], 2)
        win_prob = time[4]

        # ignore these weird endpoints
        if win_prob == 1.0:
            continue
        if win_prob == 0.0:
            continue

        # if the stated win probability led to a win
        if first_win:
            if win_prob in win_probability_master:
                (win_count, total_count) = win_probability_master[win_prob]
                win_probability_master[win_prob] = (win_count + 1, total_count + 1)
            else:
                win_probability_master[win_prob] = (1, 1)

        # otherwise, it didn't lead to a win
        else:
            if win_prob in win_probability_master:
                (win_count, total_count) = win_probability_master[win_prob]
                win_probability_master[win_prob] = (win_count, total_count + 1)
            else:
                win_probability_master[win_prob] = (0, 1)


# write this all to a CSV
with open("mens_predictions_test.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerow(["Win Probability", "Experimental Probability", "Times Team Won", "Times Probability Assigned"])
    for key in sorted(win_probability_master):
        (wins, total) = win_probability_master[key]
        writer.writerow([key, round((wins*1.0/total), 2), wins, total])
