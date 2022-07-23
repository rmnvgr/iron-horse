from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="plm_2cc2_3400",
        base_numeric_id=150,
        name="PLM 2CC2 3400",
        role="ultra_heavy_express",
        role_child_branch_num=-2,
        power_by_power_source={"DC": 5300},
        random_reverse=True,
        gen=3,
        pantograph_type="diamond-double",
        intro_year_offset=-5,  # introduce earlier than gen epoch by design
        force_default_pax_mail_livery=2,  # pax/mail cars default to second livery with this engine
        default_livery_extra_docs_examples=[
            ("COLOUR_LIGHT_BLUE", "COLOUR_WHITE"),
            ("COLOUR_PALE_GREEN", "COLOUR_WHITE"),
            ("COLOUR_DARK_GREEN", "COLOUR_WHITE"),
            ("COLOUR_BLUE", "COLOUR_BLUE"),
        ],
        sprites_complete=False,
    )

    consist.add_unit(
        type=ElectricEngineUnit, weight=105, vehicle_length=8, spriterow_num=0, repeat=2
    )

    consist.description = """ """
    consist.foamer_facts = """PLM 2CC2 3400"""

    return consist
