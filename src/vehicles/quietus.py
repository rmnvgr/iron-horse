from train import EngineConsist, ElectroDieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="quietus",
        base_numeric_id=14410,
        name="Quietus",
        role="ultra_heavy_freight",
        role_child_branch_num=-3,
        # HP matched to equivalent gen pure diesels
        power_by_power_source={
            "DIESEL": 3250,
            "AC": 6700,
        },  # based on the Stadler Eurodual, really quite high values for both diesel and el (also matches Newag Dragon, which the shape is taken from)
        tractive_effort_coefficient=0.375,  # assume slip control magic
        random_reverse=True,
        pantograph_type="z-shaped-double",
        gen=6,
        fixed_run_cost_points=500,  # run cost nerf for high power + dual mode
        intro_year_offset=2,  # introduce later than gen epoch by design
        sprites_complete=True,
    )

    consist.add_unit(
        type=ElectroDieselEngineUnit, weight=136, vehicle_length=8, spriterow_num=0
    )

    consist.description = """It'll get there and back again, in any weather."""
    consist.foamer_facts = """Stadler Eurodual, Newag Dragon, CAF Bitrac"""

    return consist
