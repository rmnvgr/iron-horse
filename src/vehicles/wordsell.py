import global_constants
from train import Train, SteamTenderLoco

vehicle = SteamTenderLoco(id = 'wordsell',
            numeric_id = 1250,
            title = 'Wordsell [Steam]',
            replacement_id = '-none',
            buy_cost = 22,
            fixed_run_cost_factor = 3.5,
            fuel_run_cost_factor = 1.0,
            speed = 80,
            power = 1550,
            weight = 126,
            tractive_effort_coefficient = 0.18,
            vehicle_length = 7,
            loading_speed = 20,
            intro_date = 1905,
            str_type_info = 'COASTER',
            vehicle_life = 40,
            trailing_part_lengths = [4],
            graphics_status = '',)

vehicle.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
