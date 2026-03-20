from manifest_protocol.engine.dice import dice


def test_dice_2d_range():
    """2D roll should always be between 2 and 12"""
    num_runs = 100
    successes = 0

    for i in range(num_runs):
        result = dice(2)
        if 2 <= result <= 12:
            successes += 1
        else:
            print(f"Failed roll: {result}")

    success_rate = successes / num_runs * 100
    print(f"2D roll success rate: {success_rate}%")

    assert successes == num_runs, "Some rolls were out of range!"
