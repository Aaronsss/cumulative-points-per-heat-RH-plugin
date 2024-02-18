''' Class ranking method: Cumulative points per final '''

import logging
import RHUtils
from eventmanager import Evt
from RHRace import StartBehavior
from Results import RaceClassRankMethod
from RHUI import UIField, UIFieldType, UIFieldSelectOption

logger = logging.getLogger(__name__)

def rank_points_heat(rhapi, race_class, args):

    heats = rhapi.db.heats_by_class(race_class.id)

    pilotresults = {}
    for heat in heats:
        races = rhapi.db.races_by_heat(heat.id)

        for race in races:
            race_result = rhapi.db.race_results(race)

            if race_result:
                for pilotresult in race_result[race_result['meta']['primary_leaderboard']]:
                    if pilotresult['pilot_id'] not in pilotresults:
                        pilotresults[pilotresult['pilot_id']] = []
                    pilotresults[pilotresult['pilot_id']].append(pilotresult)
            else:
                logger.warning("Failed building ranking, race result not available")
                return False, {}

    leaderboard = []
    for pilotresultlist in pilotresults:
        pilot_result = pilotresults[pilotresultlist]

        new_pilot_result = {}
        new_pilot_result['pilot_id'] = pilot_result[0]['pilot_id']
        new_pilot_result['callsign'] = pilot_result[0]['callsign']
        new_pilot_result['team_name'] = pilot_result[0]['team_name']
        new_pilot_result['points'] = 0
        new_pilot_result['heat'] = ''
        new_pilot_result['heat_id'] = 0
        new_pilot_result['laps'] = 0
        new_pilot_result['total_time_raw'] = 0

        for race in pilot_result:
            new_pilot_result['laps'] += race['laps']
            new_pilot_result['total_time_raw'] += race['total_time_raw']
            if 'points' in race:
                new_pilot_result['points'] += race['points']

        timeFormat = rhapi.db.option('timeFormat')
        new_pilot_result['total_time'] = str(new_pilot_result['laps']) + '/' + RHUtils.time_format(new_pilot_result['total_time_raw'], timeFormat)

        for heat in reversed(heats):
            heat_result = rhapi.db.heat_results(heat)
            if heat_result:
                heat_leaderboard = heat_result[heat_result['meta']['primary_leaderboard']]
        
                for line in heat_leaderboard:
                    if line['pilot_id'] == pilot_result[0]['pilot_id']:
                        new_pilot_result['heat'] = heat.display_name
                        new_pilot_result['heat_id'] = heat.id

        leaderboard.append(new_pilot_result)

    # Sort by points
    leaderboard = sorted(leaderboard, key = lambda x: (
        -x['heat_id'],
        -x['points'],
        -x['laps'], # reverse lap count
        x['total_time_raw'] if x['total_time_raw'] and x['total_time_raw'] > 0 else float('inf') # total time ascending except 0
    ))

    # determine ranking
    last_rank = None
    last_rank_points = 0
    for i, row in enumerate(leaderboard, start=1):
        pos = i
        row['position'] = pos

    meta = {
        'rank_fields': [{
            'name': 'heat',
            'label': "Heat"
        },{
            'name': 'total_time',
            'label': "Laps"
        },{
            'name': 'points',
            'label': "Points"
        }]
    }

    return leaderboard, meta

def register_handlers(args):
    args['register_fn'](
        RaceClassRankMethod(
            "Cumulative Points per Heat",
            rank_points_heat,
            None,
            None
        )
    )

def initialize(rhapi):
    rhapi.events.on(Evt.CLASS_RANK_INITIALIZE, register_handlers)

