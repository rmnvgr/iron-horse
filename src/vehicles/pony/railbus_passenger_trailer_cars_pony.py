from train import (
    PassengerRailbusTrailerCarConsist,
    PaxRailcarTrailerCar,
)


def main(roster_id, **kwargs):
    # --------------- pony NG----------------------------------------------------------------------

    consist = PassengerRailbusTrailerCarConsist(
        roster_id=roster_id,
        roster_id_providing_module = kwargs["roster_id_providing_module"],
        base_numeric_id=10030,
        gen=3,
        subtype="U",
        base_track_type_name="NG",
        cab_id="mumble",
        sprites_complete=True,
    )

    consist.add_unit(
        type=PaxRailcarTrailerCar, chassis="4_axle_ng_24px", tail_light="railcar_24px_1"
    )
