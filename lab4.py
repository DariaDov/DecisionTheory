profile = [
    (3, ['c', 'd', 'a', 'b']),
    (4, ['b', 'a', 'd', 'c']),
    (4, ['a', 'b', 'c', 'd'])
]

candidates = ['a', 'b', 'c', 'd']

def majority(profile, candidates):
    print("Метод відносної більшості:")

    scores = {cand: 0 for cand in candidates}

    for count, pref in profile:
        first_choice = pref[0]
        scores[first_choice] += count

    for c in candidates:
        print(f"Кандидат {c}: {scores[c]}")

    max_votes = max(scores.values())
    winners = [c for c, votes in scores.items() if votes == max_votes]

    if len(winners) > 1:
        print(f"Нічия між {winners}\n")
    else:
        print(f"Переможець {winners[0]}\n")
    
def condorcet(profile, candidates):
    print("Метод Кондорсе:")
    
    winner = None

    for c1 in candidates:
        wins_all = True
        
        for c2 in candidates:
            if c1 == c2:
                continue
            
            votes_c1 = 0
            votes_c2 = 0
            for count, pref in profile:
                if pref.index(c1) < pref.index(c2):
                    votes_c1 += count
                else:
                    votes_c2 += count
                    
            print(f"{c1} та {c2} - {votes_c1}:{votes_c2}", end="")
            if votes_c1 > votes_c2:
                print(f" - {c1} переміг")
            else:
                print(f" - {c1} не переміг")
                wins_all = False
                
        if wins_all:
            winner = c1
            break

    print(f"Переможець {winner}\n")

def alternative_voices(profile, candidates):
    print("Метод альтернативних голосів:")

    total_voters = sum(count for count, _ in profile)
    active_candidates = list(candidates)
    round_num = 1

    while True:
        print(f"Крок {round_num}:")

        current_scores = {cand: 0 for cand in active_candidates}
        
        for count, prefs in profile:
            for cand in prefs:
                if cand in active_candidates:
                    current_scores[cand] += count
                    break
                    
        for cand in active_candidates:
            print(f"  Кандидат {cand}: {current_scores[cand]}")
            
        round_winner = None
        for cand, votes in current_scores.items():
            if votes > total_voters / 2:
                round_winner = cand
                break
                
        if round_winner:
            print(f"Переможець {round_winner}\n")
            break
            
        if len(active_candidates) <= 1:
            break
            
        min_votes = min(current_scores.values())
        to_remove = sorted([cand for cand, votes in current_scores.items() if votes == min_votes])[0]
        
        active_candidates.remove(to_remove)
        print(f"  Кандидат {to_remove} вибуває")
        round_num += 1

majority(profile, candidates)
condorcet(profile, candidates)
alternative_voices(profile, candidates)