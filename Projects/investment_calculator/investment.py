import argparse
from calculators.lumpsum import lumpsum


def argument_parser():
    """
    This method creates an argument parser
    """
    parser = argparse.ArgumentParser(
        description="Investment Calculator")
    parser.add_argument('lumpsum',type=str)
    parser.add_argument(
        'total_investement', 
        type=int,
        help="present value of investment")
    parser.add_argument(
        'intrest_rate',
        type=int,
        help="rate of intrest")
    parser.add_argument(
        'time_period',
        type=int,
        help="time in years")
    return parser

if __name__ == "__main__":
    args = argument_parser().parse_args()
    result = lumpsum(
        prinicpal= args.total_investement,
        intrest_rate=args.intrest_rate,
        time_in_years=args.time_period
    )
    print(f"Your investment of {args.total_investement} will be {result} in next {args.time_period} years")


