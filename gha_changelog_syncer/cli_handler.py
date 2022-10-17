import argparse
import datetime

import dateutil.parser
import dotenv

import gha_changelog_syncer


def handle():
    dotenv.load_dotenv()

    parser = argparse.ArgumentParser(
        description="Send a pull request description to a Notion Database."
    )
    parser.add_argument("--title", help="Pull request title")
    parser.add_argument("--description", help="Pull request description", default="")
    parser.add_argument(
        "--merged_at",
        help="Pull request merge date (e.g. 2011-01-26T19:01:12Z)",
        default=datetime.datetime.utcnow().isoformat(),
    )

    args = parser.parse_args()
    merged_at = dateutil.parser.isoparse(args.merged_at)

    gha_changelog_syncer.run(args.title, args.description, merged_at)
