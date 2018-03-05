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


class PlayerData:
    """Handles Player Data requests"""

    def __init__(self, season, player):
        self.season_data = season.season_data
        self.profile_data = self._get_profile(player)
        self.match_data = self._get_match_data()

    def _get_profile(self, player):
        """
        Returns profile data of the player

        @param player - id or name of the player to look up
        """
        try:
            try:
                player = int(player)
            except ValueError:
                player = player.lower()
            player_list = self.season_data["proPlayers"]
            for p in player_list:
                if p["id"] == player:
                    return p
                if p["name"].lower() == player:
                    return p
        except Exception as e:
            error_msg = ("Failed to retrieve player profile data: {}"
                         "".format(str(e)))
            raise PlayerDataException(error_msg)

    def _get_match_data(self):
        """
        Returns match data related to player
        """
        try:
            match_data = []
            player_id = self.profile_data["id"]
            matches = self.season_data["stats"]["actualPlayerStats"]
            for match in matches:
                if player_id == match[0]:
                    match_data.append(match)
            match_data.sort(key=lambda x: x[2])  # sort by match id
            return match_data
        except Exception as e:
            error_msg = ("Failed to retrieve player match data: {}"
                         "".format(str(e)))
            raise PlayerDataException(error_msg)

    def get_player_id(self):
        """
        Returns the player id
        """
        try:
            return self.profile_data["id"]
        except Exception as e:
            error_msg = ("Failed to retrieve player id: {}"
                         "".format(str(e)))
            raise PlayerDataException(error_msg)

    def get_name(self):
        """
        Returns the player name
        """
        try:
            return self.profile_data["name"]
        except Exception as e:
            error_msg = ("Failed to retrieve player name: {}"
                         "".format(str(e)))
            raise PlayerDataException(error_msg)

    def get_photo_url(self):
        """
        Returns the photo url of the player
        """
        try:
            return self.profile_data["photoUrl"]
        except Exception as e:
            error_msg = ("Failed to retrieve photo url: {}"
                         "".format(str(e)))
            raise PlayerDataException(error_msg)

    def get_positions(self):
        """
        Returns a list of all the player's positions
        """
        try:
            return self.profile_data["positions"]
        except Exception as e:
            error_msg = ("Failed to retrieve a list of player positions: {}"
                         "".format(str(e)))
            raise PlayerDataException(error_msg)

    def get_team_id(self):
        """
        Returns the player's team id
        """
        try:
            return self.profile_data["proTeamId"]
        except Exception as e:
            error_msg = ("Failed to retrieve the player's team id: {}"
                         "".format(str(e)))
            raise PlayerDataException(error_msg)

    def get_riot_id(self):
        """
        Returns the player's riot id
        """
        try:
            return self.profile_data["riotId"]
        except Exception as e:
            error_msg = ("Failed to retrieve the player's riot id: {}"
                         "".format(str(e)))
            raise PlayerDataException(error_msg)

    def get_trends_by_week(self):
        """
        Returns a dictionary of all the player's weekly trends
        """
        try:
            return self.profile_data["trendsByWeek"]
        except Exception as e:
            error_msg = ("Failed to retrieve weekly trends: {}"
                         "".format(str(e)))
            raise PlayerDataException(error_msg)

    def get_matches_played(self):
        """
        Returns the total matches played
        """
        try:
            return len(self.match_data)
        except Exception as e:
            error_msg = ("Failed to retrieve number of matches played: {}"
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
        Returns match stats of a player given a number in a range
        from the first match to the most recent match

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
