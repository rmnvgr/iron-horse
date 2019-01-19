from train import MailEngineRailcarConsist, DieselRailcarBaseUnit

def main():    
    consist = MailEngineRailcarConsist(id='scooby',
                                       base_numeric_id=3070,
                                       name='Scooby',
                                       role='mail_railcar',
                                       power=420,
                                       gen=4,
                                       sprites_complete=True,
                                       intro_date_offset=-5)  # introduce early by design
    
    consist.add_unit(type=DieselRailcarBaseUnit,
                     weight=37,
                     vehicle_length=8,
                     # set capacity for freight; mail will be automatically calculated; match to 8/8 mail car for this gen
                     capacity=22,
                     chassis='railcar')

    return consist