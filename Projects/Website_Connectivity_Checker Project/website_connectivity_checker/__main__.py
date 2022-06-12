#  Including a __main__.py file in a Python package enables you to run the package 
# as an executable program using the command python -m <package_name>.

""" It is a Entry-point script """

import sys
import pathlib
from website_connectivity_checker.cli import read_user_cli_args, display_check_result
from website_connectivity_checker.checker import site_is_online

def main():
    """Run RP Checker."""
    user_args = read_user_cli_args()
    urls = _get_websites_urls(user_args)
    if not urls:
        print("Error: no URLs to check", file=sys.stderr)
        sys.exit(1)
    _synchronous_check(urls)

#  _get_websites_urls() defines a conditional that checks if the user has provided a URLs file. 
# If so, then the if block augments the list of target URLs resulting from
#  calling _read_urls_from_file() with the file provided in the user_args.input_file 
# command-line argument.

def _get_websites_urls(user_args):
    urls = user_args.urls
    if user_args.input_file:
        urls += _read_urls_from_file(user_args.input_file)
    return urls

def _read_urls_from_file(file):
    file_path = pathlib.Path(file)
    if file_path.is_file():
        with file_path.open() as urls_file:
            urls = [url.strip() for url in urls_file]
            if urls:
                return urls
            print(f"Error: empty input file, {file}", file=sys.stderr)
    else:
        print("Error: input file not found", file=sys.stderr)
    return []

def _synchronous_check(urls):
    for url in urls:
        error = ""
        try:
            result = site_is_online(url)
        except Exception as e:
            result = False
            error = str(e)
        display_check_result(result, url, error)


if __name__ == "__main__":
    main()