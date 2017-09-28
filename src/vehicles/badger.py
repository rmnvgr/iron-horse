import global_constants
from train import EngineConsist, ElectricLoco

consist = EngineConsist(id='badger',
                        base_numeric_id=450,
                        title='Flying Badger [Electric]',
                        power=6400,
                        speed=125,
                        type_base_buy_cost_points=71,  # dibble buy cost for game balance
                        vehicle_generation=5)

consist.add_unit(type=ElectricLoco,
                 weight=105,
                 vehicle_length=8,
                 spriterow_num=0)

consist.add_model_variant(start_date=0,
                          end_date=global_constants.max_game_date)
