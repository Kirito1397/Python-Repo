import argparse

def read_user_cli_args():
    """ Handle the CLI arguments and options"""
    parser = argparse.ArgumentParser(prog="website_connectivity_checker", description="Check the availability of websites")

    # Provide Website URLs argument at the Command Line
    parser.add_argument(
        "-u",
        "--urls",
        metavar="URLs",
        nargs="+",
        type = str,
        default=[],
        help="Enter one or more website URLs.",
    )

    # Load Website URLs From a File argument at CLI
    parser.add_argument(
        "-f",
        "--input-file",
        metavar="Input File",
        type=str,
        default="",
        help="Read URLs from the file.",
    )

    return parser.parse_args()

def display_check_result(result, url, error=""):
    """ """
    print(f"The status of website {url} is ", end="" )
    if result:
        print("'Online' 👍")
    else:
        print(f'"Offline?" 👎 \n  Error: "{error}"')

"""" 
metavar : sets a name for the argument in usage or help messages.
nargs   : tells argparse to accept a list of command-line arguments after the -u or --urls switch.
type    : sets the data type of the command-line arguments, which is str in this argument.
default : sets the command-line argument to an empty list by default.
help    : provides a help message for the user.
"""