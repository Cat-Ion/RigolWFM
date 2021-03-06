import argparse
import wfme

def main():
    parser = argparse.ArgumentParser(
        prog='wfm_parse',
        description='Parse Rigol WFM files.'
    )
    parser.add_argument(
        '-t',
        choices=( '1000d', '1000e', '1000z', '4000', '6000'),
        required=True,
        help='the type of Rigol WFM file'
    )
    parser.add_argument('filename')
    args = parser.parse_args()
    
    description = wfme.describe(args.filename, kind=args.t)
    print(description)


if __name__ == "__main__":
    main()
