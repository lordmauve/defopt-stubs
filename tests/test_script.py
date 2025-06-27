from defopt import run, bind, bind_known


def main(value: int, *, times: int = 1) -> None:
    """Print a value multiple times.

    :param value: Value to display
    :param times: Number of repetitions
    """
    for _ in range(times):
        print(value)


def demo_bind() -> None:
    call = bind(main, argv=["1", "--times", "2"])
    call()
    call2, rest = bind_known(main, argv=["2", "--times", "3"])
    call2()


if __name__ == "__main__":
    demo_bind()
    run(main)
