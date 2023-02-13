n = int(input())
team1_score = 0
team2_score = 0
team1_time = 0
team2_time = 0

for _ in range(n):
  team_str, time_str = input().split()
  team = int(team_str)
  time_sec = int(time_str[:2]) * 60 + int(time_str[3:])
  
  if team == 1:
    team1_score += 1
  else:
    team2_score += 1
  
  if team1_score != team2_score:
    if team1_score > team2_score:
      team1_time += time_sec
    else:
      team2_time += time_sec

print(team1_time)
print(team2_time)