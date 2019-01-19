from train import EngineConsist, DieselEngineUnit


def main(roster):
    consist = EngineConsist(roster=roster,
                            id='oribi',
                            base_numeric_id=1980,
                            name='Oribi',
                            power=450,
                            base_track_type='NG',
                            intro_date=1960)

    consist.add_unit(type=DieselEngineUnit,
                     weight=65,
                     vehicle_length=8,
                     capacity=30,
                     spriterow_num=0)

    return consist
