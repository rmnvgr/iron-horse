from train import MailEngineRailcarConsist, ElectricRailcarUnit

def main():    
    consist = MailEngineRailcarConsist(id='pylon',
                                       base_numeric_id=2120,
                                       name='Pylon',
                                       role='mail_railcar',
                                       power=1000,
                                       pantograph_type='z-shaped-single',
                                       easter_egg_haulage_speed_bonus=True,
                                       gen=6,
                                       sprites_complete=False,
                                       intro_date_offset=-3)  # introduce early by design
    
    consist.add_unit(type=ElectricRailcarUnit,
                     weight=45,
                     vehicle_length=8,
                     # set capacity for freight; mail will be automatically calculated; match to 8/8 mail car for this gen
                     capacity=24,
                     chassis='railcar')

    return consist