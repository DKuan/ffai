from ffai.ai.competition import Competition
import examples.scripted_bot_example
import examples.grodbot
from copy import deepcopy
from ffai.core.load import get_team, get_rule_set, get_config

config = get_config('ff-11.json')

# Random vs. random
competition = Competition('MyCompetition', competitor_a_team_id='human-1', competitor_b_team_id='human-2', competitor_a_name='random', competitor_b_name='random', config=config)
results = competition.run(num_games=2)
results.print()

'''
# Random vs. idle
config.time_limits.game_time_limit = 10  # 10 second time limit per game
config.time_limits.turn_time_limit = 1  # 1 second time limit per turn
competition = Competition('MyCompetition', competitor_a_team_id='human-1', competitor_b_team_id='human-2', competitor_a_name='random', competitor_b_name='idle', config=config)
results = competition.run(num_games=2)
results.print()

# Random vs. violator
config.time_limits.game_time_limit = 60  # 60 second time limit per game
config.time_limits.turn_time_limit = 1  # 1 second time limit per turn
config.time_limits.opp__time_limit = 1  # 1 second time limit per opponent choice
config.time_limits.violation_threshold = 1  # 1 violation limit 
competition = Competition('MyCompetition', competitor_a_team_id='human-1', competitor_b_team_id='human-2', competitor_a_name='random', competitor_b_name='violator', config=config)
results = competition.run(num_games=2)
results.print()

# Random vs. init crash
config.time_limits.game_time_limit = 60  # 60 second time limit per game
config.time_limits.turn_time_limit = 1  # 1 second time limit per turn
config.time_limits.opp_time_limit = 1  # 1 second time limit per opponent choice
config.time_limits.violation_threshold = 1  # 1 violation threshold 
config.time_limits.init_time_limit = 20  # 2 init limit 
competition = Competition('MyCompetition', competitor_a_team_id='human-1', competitor_b_team_id='human-2', competitor_a_name='random', competitor_b_name='init-crash', config=config)
results = competition.run(num_games=2)
results.print()

# Random vs. crash
config.time_limits.game_time_limit = 32  # 32 second time limit per game
config.time_limits.turn_time_limit = 1  # 1 second time limit per turn
competition = Competition('MyCompetition', competitor_a_team_id='human-1', competitor_b_team_id='human-2', competitor_a_name='random', competitor_b_name='crash', config=config)
results = competition.run(num_games=2)
results.print()
'''