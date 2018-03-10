#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

FANTASY_SEASON_START = 1
FANTASY_SEASON_CURRENT = 16
REGIONS_SUPPORTED = ["na", "lan", "las", "euw", "eune", "oce"]


class SeasonDataException(Exception):
    """Handles SeasonData Exceptions"""


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
