# Fantasy LCS API Wrapper

Created an unofficial Fantasy LCS API in Python 3.6.

# Installation

Currently no setup script yet. For the moment you can move the folder to your site packages or move it locally to your working directory.

# Documentation

**Initialization**

```python
>>> from fantasyleague import FantasyLeague
>>> test = FantasyLeague("na", 1)
```

----------

**Get Fantasy Names**

Returns the name of the fantasy league

```python
>>> test.get_fantasy_name()
test
```

----------

**Get Fantasy Size**

Returns the number of teams in the fantasy league

```python
>>> test.get_fantasy_size()
4
```

----------

**Get Current Week**

Returns the current week number in the fantasy league

```python
>>> test.get_current_week()
12
```

----------

**Get Fantasy Status**

Returns the status of the fantasy league

```python
>>> test.get_fantasy_status()
IN_SEASON
```

----------

**Get Fantasy Game Mode**

Returns the mode of what games count towards fantasy. (Results vary, it could be BEST_1 (Best of 1), ALL (All games), etc..)

```python
>>> test.get_games_counted()
ALL
```

----------

**Get Fantasy Point Format**

Returns a dictionary of stats with how many points counted per stat

```python
>>> test.get_points_per_stat()
{
	'kills': 2,
	'deaths': -0.5,
	'assists': 1.5,
	'minionKills': 0.01,
	'doubleKills': 0,
	'tripleKills': 2,
	'quadraKills': 3,
	'pentaKills': 5,
	'killOrAssistBonus': 2,
	'firstBlood': 2,
	'towerKills': 1,
	'baronKills': 2,
	'dragonKills': 1,
	'gameVictory': 2,
	'gameDefeat': 0,
	'quickWinBonus': 0
}
```

----------

**Get Fantasy Teams**

Returns a list of fantasy teams

```python
>>> test.get_fantasy_teams()
[{
	'id': 1,
	'name': 'team number one',
	'summonerName': 'mhixson1'
}, {
	'id': 2,
	'name': 'team three',
	'summonerName': 'mhixson3'
}, {
	'id': 3,
	'name': 'TWO!!!',
	'summonerName': 'mhixson2'
}, {
	'id': 4,
	'name': 'The fourth and final',
	'summonerName': 'mhixson4'
}]
```

----------

**Get Fantasy Matches**

Returns a list of all the fantasy matches

```python
>>> test.get_fantasy_matches()
[{
	'id': 45,
	'week': 1,
	'redTeam': {
		'id': 4,
		'roster': {
			'TOP_LANE': [{
				'targetType': 'player',
				'targetId': 41,
				'position': 'TOP_LANE',
				'slot': 0
			}],
			'JUNGLER': [{
				'targetType': 'player',
				'targetId': 93,
				'position': 'JUNGLER',
				'slot': 0
			}],
			'MID_LANE': [{
				'targetType': 'player',
				'targetId': 100,
				'position': 'MID_LANE',
				'slot': 0
			}],
			'AD_CARRY': [{
				'targetType': 'player',
				'targetId': 102,
				'position': 'AD_CARRY',
				'slot': 0
			}],
			'SUPPORT': [{
				'targetType': 'player',
				'targetId': 38,
				'position': 'SUPPORT',
				'slot': 0
			}],
			'FLEX': [{
				'targetType': 'player',
				'targetId': 44,
				'position': 'FLEX',
				'slot': 0
			}],
			'TEAM': [{
				'targetType': 'team',
				'targetId': 6,
				'position': 'TEAM',
				'slot': 0
			}],
			'RESERVE': [{
				'targetType': 'player',
				'targetId': 92,
				'position': 'RESERVE',
				'slot': 0
			}, {
				'targetType': 'player',
				'targetId': 105,
				'position': 'RESERVE',
				'slot': 0
			}, {
				'targetType': 'team',
				'targetId': 16,
				'position': 'RESERVE',
				'slot': 0
			}]
		}
	},
...
...
}]
```

----------

**Get Fantasy Roster Updates**

Returns a list of all the roster updates

```python
>>> test.get_fantasy_roster_updates()
[{
	'time': '2014-02-13T22:33:09',
	'fantasyTeamId': 1,
	'targetType': 'player',
	'targetId': 4,
	'addition': False
}, {
	'time': '2014-02-13T22:33:09',
	'fantasyTeamId': 1,
	'targetType': 'player',
	'targetId': 59,
	'addition': True
}]
```

----------

**Get Fantasy Trades Created**

Returns a list of all the trades made

(Example below taken from a different fantasy league)

```python
>>> test.get_fantasy_trades()
[{
	'id': 717508,
	'firstTeam': 3550583,
	'secondTeam': 3551681,
	'status': 'INVALIDATED',
	'lastModified': '2018-01-20T19:39:01',
	'entries': [{
		'targetType': 'player',
		'targetId': 1791,
		'direction': 'SECOND_TO_FIRST'
	}, {
		'targetType': 'player',
		'targetId': 1801,
		'direction': 'FIRST_TO_SECOND'
	}]
}, {
	'id': 740806,
	'firstTeam': 3550648,
	'secondTeam': 3550628,
	'status': 'SUCCESSFUL',
	'lastModified': '2018-02-04T20:08:45',
	'entries': [{
		'targetType': 'player',
		'targetId': 1722,
		'direction': 'SECOND_TO_FIRST'
	}, {
		'targetType': 'player',
		'targetId': 1762,
		'direction': 'FIRST_TO_SECOND'
	}]
}]
```

----------

**Get Fantasy Roster Posession Limits**

Returns the number limit of the roles you're allowed to have

```python
>>> test.get_fantasy_roster_limits()
{
	'TOP_LANE': 1,
	'JUNGLER': 1,
	'MID_LANE': 1,
	'AD_CARRY': 1,
	'SUPPORT': 1,
	'FLEX': 1,
	'TEAM': 1,
	'RESERVE': 3
}
```

----------

**Get Fantasy Role Posession Limit**


Returns the number limit of the same role you're allowed to have

```python
>>> test.get_fantasy_role_limit()
2
```
