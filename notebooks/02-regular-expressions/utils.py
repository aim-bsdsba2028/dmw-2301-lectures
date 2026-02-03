"""Helper functions for the regular expressions notebook"""


def highlight_matches(regex_iter, markers=['\033[1m[', ']\033[0m']):
    """Highlight the matches found by the regex using the specified markers

    Parameters
    ----------
    regex_iter : list of RegEx match object
        List containing the RegEx match result
    text : str
        Text in which the regular expression was applied to
    markers : list of str
        Markers to be used markers[0] is placed on the left, while
        markers[1] is placed on the right

    Returns
    -------
    highlighted_text : str
        Text in which the regex matches has been highlighted
    """
    text = regex_iter[0].string

    # Add markers
    extra = 0
    for match in regex_iter:
        start = match.start()
        end = match.end()
    
        text = text[:start + extra] + markers[0] + text[start + extra:]
        extra += len(markers[0])
        text = text[:end + extra] + markers[1] + text[end + extra:]
        extra += len(markers[1])

    return text
