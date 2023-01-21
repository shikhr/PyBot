replments_params = {
    "_": "__",
    " ": "_",
    "-": "--",
    "?": "~q",
    "&": "~a",
    "%": "~p",
    "#": "~h",
    "/": "~s",
    "\\": "~b",
    "<": "~l",
    ">": "~g",
    '"': "''",
}
replments_key = replments_params.copy()
del replments_key["-"]

allowed_ext = ["png", "gif", "jpg", "webp"]


def gen_meme_url(args):
    if len(args) == 0:
        return "No arguments supplied! Use .mkmem --help to see how to use the command."
    generator = {"key": "", "params": [], "ext": "png"}
    generator["key"] = "".join([replments_key.get(c, c) for c in args[0]])
    if args[-1] in allowed_ext:
        generator["ext"] = args[-1].lower()
    for word in args[1:-1]:
        generator["params"].append("".join([replments_params.get(c, c) for c in word]))
    gen_url = (
        "/".join([generator["key"]] + generator["params"]) + f'.{generator["ext"]}'
    )
    return f"please wait while the meme is generating:\n https://api.memegen.link/images/{gen_url}"
