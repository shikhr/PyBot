replments = {
    "_": "__",
    " ": "_",
    "-": "--",
    "?": "~q",
    "&": "~a",
    "/": "~s",
    "\\": "~b",
    "#": "~h",
    '""': "''",
}


def gen_meme_url(args):
    if len(args) == 0:
        return "No arguments supplied! Use .mkmem --help to see how to use the command."
    params = []
    for word in args:
        params.append("".join([replments.get(c, c) for c in word]))
    params[0] = params[0].replace("--", "-")
    gen_url = "/".join(params[:-1]) + f".{params[-1]}"
    return f"please wait while the meme is generating:\n https://api.memegen.link/images/{gen_url}"
