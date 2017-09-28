import global_constants
from train import EngineConsist, DieselRailcar

consist = EngineConsist(id='antlion',
                        base_numeric_id=1550,
                        title='Antlion [Diesel]',
                        power=350,
                        speed=55,
                        type_base_running_cost_points=-32,  # dibble running costs for game balance
                        intro_date=1950)

consist.add_unit(type=DieselRailcar,
                 weight=75,
                 vehicle_length=8,
                 capacity_pax=45,
                 spriterow_num=0)

consist.add_model_variant(start_date=0,
                          end_date=global_constants.max_game_date)
