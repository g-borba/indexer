from argparse import ArgumentParser
from domain.count_word_occurrences import CountWordOcurrences
from domain.count_top_words import CountTopWords
from domain.tfidf import SearchRelevantFilesByTerms


def main():
    args = get_user_args()

    if args.freq:
        service = CountTopWords(file_name=args.freq[1])
        service.count_top_words(word_count=(int(args.freq[0])))

    if args.freq_word:
        service = CountWordOcurrences(file_name=args.freq_word[1])
        service.count_occurrences(target_word=args.freq_word[0])

    if args.search:
        service = SearchRelevantFilesByTerms(file_names=args.search[1:])
        service.list_relevant_files(terms=args.search[0:])


def get_user_args():
    parser = ArgumentParser(description="Process some files.")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--freq",
        nargs=2,
        metavar=("N", "FILE"),
        help="Display the N most common words in a file.",
    )
    group.add_argument(
        "--freq-word",
        nargs=2,
        metavar=("WORD", "FILE"),
        help="Display the number of occurrences of a word in a file.",
    )
    group.add_argument(
        "--search",
        nargs="+",
        metavar=("TERM(s)", "FILE(s)"),
        help="Search for one or more terms in one or more files.",
    )

    return parser.parse_args()


if __name__ == "__main__":
    main()
