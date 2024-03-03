from train import MailEngineRailcarConsist, DieselRailcarMailUnit


def main(roster_id, **kwargs):
    consist = MailEngineRailcarConsist(
        roster_id=roster_id,
        id="ruby",
        base_numeric_id=28310,
        name="Ruby",
        role="mail_railcar",
        role_child_branch_num=1,
        base_track_type_name="NG",
        power_by_power_source={
            "DIESEL": 600,
        },
        gen=4,
        extended_vehicle_life=True,  # extended vehicle life for all this generation of NG eh
        sprites_complete=False,
    )

    consist.add_unit(
        type=DieselRailcarMailUnit,
        weight=18,
        effect_z_offset=11,  # reduce smoke z position to suit NG engine height
        chassis="railcar_ng_24px",
        tail_light="railcar_24px_1",
    )

    consist.description = """"""
    consist.foamer_facts = """CFC Autorail Billard, CFC X2000/X5000"""

    return consist
