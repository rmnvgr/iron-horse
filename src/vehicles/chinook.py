import global_constants
from train import EngineConsist, DieselLoco

consist = EngineConsist(id='chinook',
                        base_numeric_id=120,
                        title='Chinook [Diesel]',
                        power=3000,
                        speed=75,
                        type_base_buy_cost_points=30,  # dibble buy cost for game balance
                        vehicle_generation=4)

consist.add_unit(type=DieselLoco,
                 weight=80,
                 vehicle_length=6,
                 spriterow_num=0)

consist.add_unit(type=DieselLoco,
                 weight=80,
                 vehicle_length=6,
                 spriterow_num=1)

consist.add_model_variant(start_date=0,
                          end_date=global_constants.max_game_date)
