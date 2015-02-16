import global_constants
from train import TypeConfig, WagonConsist, MailCar

cargo_graphics_mappings = {} # template needs this, but mail car has zero cargo-specific graphics, all generic

type_config_normal = TypeConfig(base_id = 'mail_car',
                template = 'car_with_open_doors_during_loading.pynml',
                num_cargo_rows = 1, # template needs this, but mail car has zero cargo-specific graphics, all generic
                class_refit_groups = ['mail', 'express_freight'],
                cargo_graphics_mappings = cargo_graphics_mappings,
                label_refits_allowed = list(cargo_graphics_mappings.keys()) ,
                label_refits_disallowed = global_constants.disallowed_refits_by_label['non_freight_special_cases'],
                autorefit = True,
                default_cargo = 'MAIL',
                default_capacity_type = 'capacity_mail')

type_config_narrow_gauge = TypeConfig(base_id = 'mail_car_ng',
                template = 'car_with_open_doors_during_loading.pynml',
                num_cargo_rows = 1, # template needs this, but mail car has zero cargo-specific graphics, all generic
                class_refit_groups = ['mail', 'express_freight'],
                cargo_graphics_mappings = cargo_graphics_mappings,
                label_refits_allowed = list(cargo_graphics_mappings.keys()) ,
                label_refits_disallowed = [],
                autorefit = True,
                default_cargo = 'MAIL',
                default_capacity_type = 'capacity_mail',
                track_type = 'NG')

def main():
    #--------------- brit ----------------------------------------------------------------------
    consist = WagonConsist(type_config = type_config_normal,
                        title = '[Mail Car]',
                        roster = 'brit',
                        wagon_generation = 1,
                        replacement_id = '-none',
                        intro_date = 1860,
                        vehicle_life = 40,
                        speedy = True,
                        use_legacy_spritesheet = True)

    consist.add_unit(MailCar(consist = consist,
                            capacity_mail = 30,
                            weight = 29,
                            vehicle_length = 7))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0)


    consist = WagonConsist(type_config = type_config_normal,
                        title = '[Mail Car]',
                        roster = 'brit',
                        wagon_generation = 2,
                        replacement_id = '-none',
                        intro_date = 1925,
                        vehicle_life = 40,
                        speedy = True,
                        use_legacy_spritesheet = True)

    consist.add_unit(MailCar(consist = consist,
                            capacity_mail = 45,
                            weight = 30,
                            vehicle_length = 7))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0)


    consist = WagonConsist(type_config = type_config_normal,
                        title = '[Mail Car]',
                        roster = 'brit',
                        wagon_generation = 3,
                        replacement_id = '-none',
                        intro_date = 1985,
                        vehicle_life = 40,
                        speedy = True,
                        use_legacy_spritesheet = True)

    consist.add_unit(MailCar(consist = consist,
                            capacity_mail = 60,
                            weight = 31,
                            vehicle_length = 8))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0)


    consist = WagonConsist(type_config = type_config_narrow_gauge,
                        title = '[Mail Car]',
                        roster = 'brit',
                        wagon_generation = 1,
                        replacement_id = '-none',
                        intro_date = 1860,
                        vehicle_life = 40,
                        use_legacy_spritesheet = True)

    consist.add_unit(MailCar(consist = consist,
                            capacity_freight = 12,
                            capacity_mail = 24,
                            weight = 5,
                            vehicle_length = 5))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0)


    #--------------- soam ----------------------------------------------------------------------
    consist = WagonConsist(type_config = type_config_normal,
                        title = '[Mail Car]',
                        roster = 'soam',
                        wagon_generation = 1,
                        replacement_id = '-none',
                        intro_date = 1860,
                        vehicle_life = 40,
                        speedy = True)

    consist.add_unit(MailCar(consist = consist,
                            capacity_mail = 30,
                            weight = 29,
                            vehicle_length = 7))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0)


    consist = WagonConsist(type_config = type_config_normal,
                        title = '[Mail Car]',
                        roster = 'soam',
                        wagon_generation = 2,
                        replacement_id = '-none',
                        intro_date = 1920,
                        vehicle_life = 40,
                        speedy = True)

    consist.add_unit(MailCar(consist = consist,
                            capacity_mail = 45,
                            weight = 30,
                            vehicle_length = 8))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0)


    consist = WagonConsist(type_config = type_config_normal,
                        title = '[Mail Car]',
                        roster = 'soam',
                        wagon_generation = 3,
                        replacement_id = '-none',
                        intro_date = 1980,
                        vehicle_life = 40,
                        speedy = True)

    consist.add_unit(MailCar(consist = consist,
                            capacity_mail = 60,
                            weight = 31,
                            vehicle_length = 8))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0)

