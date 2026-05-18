# 2026-05-18

import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:

    scores = scores.drop(columns=['id'])

    if scores.empty:
        dictionary = {'rank': []}
        scores['rank'] = dictionary['rank']
        return scores

    scores = scores.sort_values(by=['score'], ascending=False).reset_index(drop=True)

    dictionary = {'rank': []}
    last_score = scores['score'][0]
    rank = 1

    for i, row in scores.iterrows():
        if last_score == row.score:
            dictionary['rank'].append(rank)
        else:
            rank += 1
            dictionary['rank'].append(rank)
        last_score = row.score

    scores['rank'] = dictionary['rank']

    return scores