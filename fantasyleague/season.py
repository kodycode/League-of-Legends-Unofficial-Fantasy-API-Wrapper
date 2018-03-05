#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

FANTASY_SEASON_START = 1
FANTASY_SEASON_CURRENT = 16
REGIONS_SUPPORTED = ["na", "lan", "las", "euw", "eune", "oce"]


class SeasonDataException(Exception):
    """Handles SeasonData Exceptions"""


class PlayerDataException(Exception):
    """Handles PlayerData Exceptions"""


class SeasonData:
    """Handles Season Data requests"""

    def __init__(self, region, season):
        self.season_data = self._get_season_data(region, int(season))

    def _get_season_data(self, region, season):
        """
        Returns season data

        @param region - region that fantasy season exists in
        @param season - fantasy lcs season number
                        (don't confuse this with the season number of LoL)
        """
        try:
            region = region.lower()
            if region not in REGIONS_SUPPORTED:
                raise Exception("Region not supported: {}"
                                "".format(region))
            if not FANTASY_SEASON_START <= season <= FANTASY_SEASON_CURRENT:
                raise Exception("Season does not exist")
            FANTASY_SEASON_URL = ("https://fantasy.{}.lolesports.com/en-US/api/"
                                  "season/{}".format(region, season))
            data = requests.get(FANTASY_SEASON_URL)
            data.raise_for_status()
            return data.json()
        except Exception as e:
            error_msg = ("Failed to retrieve fantasy season data: {}"
                         "".format(str(e)))
            raise SeasonDataException(error_msg)


class PlayerStats:
    """Handles Player Stat requests"""

    def __init__(self, season_data, player_id):
        self.match_data = self._get_match_data(season_data, player_id)

    def _get_match_data(self, season_data, player_id):
        """
        Returns match data related to player

        @param season_data - data of the season to look into
        @param player_id - id of the player to look up
        """
        try:
            match_data = []
            player_id = int(player_id)
            matches = season_data["stats"]["actualPlayerStats"]
            for match in matches:
                if player_id == match[0]:
                    match_data.append(match)
            match_data.sort(key=lambda x: x[2])
            return match_data
        except Exception as e:
            error_msg = ("Failed to retrieve player match data: {}"
                         "".format(str(e)))
            raise PlayerDataException(error_msg)

    def get_all_match_stats(self):
        """
        Returns a list of all matches played by the player
        """
        try:
            return self.match_data
        except Exception as e:
            error_msg = ("Failed to retrieve all match stats: {}"
                         "".format(str(e)))
            raise PlayerDataException(error_msg)

    def get_match_stats(self, match_number):
        """
        Returns stats of a player from a match

        @param match_number - # of the match to get
        """
        try:
            match_number = int(match_number)
            if not 0 <= match_number < len(self.match_data):
                raise Exception("Specified number is out of the match range: "
                                "{}".format(match_number))
            match_stats = self.match_data[match_number]
            return match_stats
        except Exception as e:
            error_msg = ("Failed to retrieve match stats: {}"
                         "".format(str(e)))
            raise PlayerDataException(error_msg)
