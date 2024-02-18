from train import AutomobileLowFloorCarConsist, AutomobileCarAsymmetric


def main(roster_id, **kwargs):
    # --------------- standard gauge ---------------------------------------------------------------
    # intro gen 4

    consist = AutomobileLowFloorCarConsist(
        roster_id=roster_id, base_numeric_id=14890, gen=4, subtype="B"
    )

    consist.add_unit(
        type=AutomobileCarAsymmetric, chassis="2_axle_running_gear_only_24px"
    )

    consist = AutomobileLowFloorCarConsist(
        roster_id=roster_id, base_numeric_id=14900, gen=4, subtype="C"
    )

    consist.add_unit(
        type=AutomobileCarAsymmetric, chassis="4_axle_running_gear_only_32px"
    )

    consist = AutomobileLowFloorCarConsist(
        roster_id=roster_id, base_numeric_id=14910, gen=5, subtype="B"
    )

    consist.add_unit(
        type=AutomobileCarAsymmetric, chassis="2_axle_running_gear_only_24px"
    )

    consist = AutomobileLowFloorCarConsist(
        roster_id=roster_id, base_numeric_id=14920, gen=5, subtype="C"
    )

    consist.add_unit(
        type=AutomobileCarAsymmetric, chassis="4_axle_running_gear_only_32px"
    )
